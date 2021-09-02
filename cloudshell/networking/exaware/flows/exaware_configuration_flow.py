#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.shell.flows.configuration.basic_flow import AbstractConfigurationFlow
from cloudshell.shell.flows.utils.networking_utils import UrlParser

from cloudshell.networking.exaware.command_actions.save_restore_actions import (
    SaveRestoreActions,
)
from cloudshell.networking.exaware.command_actions.system_actions import SystemActions
from cloudshell.networking.exaware.helpers.exceptions import ExawareSaveRestoreException


class ExawareConfigurationFlow(AbstractConfigurationFlow):
    DEFAULT_CONFIG_NAME = "Quali.cfg"
    REMOTE_PROTOCOLS = ["ftp", "tftp", "scp"]
    RESTORE_TYPE_MAP = {"append": "merge", "override": "replace"}

    def __init__(self, cli_handler, resource_config, logger):
        super(ExawareConfigurationFlow, self).__init__(logger, resource_config)
        self._cli_handler = cli_handler

    @property
    def _file_system(self):
        """Determine device file system type."""
        return "local"

    def _save_flow(self, folder_path, configuration_type, vrf_management_name=None):
        """Execute flow which save selected file to the provided destination.

        :param folder_path: destination path where file will be saved
        :param configuration_type: source file, which will be saved
        :param vrf_management_name: Virtual Routing and Forwarding Name
        :return: saved configuration file name
        """
        if not configuration_type.endswith("-config"):
            configuration_type += "-config"

        if configuration_type not in ["running-config"]:
            raise ExawareSaveRestoreException(
                "Device doesn't support saving '{}' configuration type".format(
                    configuration_type
                ),
            )

        url = UrlParser().parse_url(folder_path)
        scheme = url.get("scheme")
        avail_protocols = self.REMOTE_PROTOCOLS + [self._file_system]
        if scheme not in avail_protocols:
            raise ExawareSaveRestoreException(
                f"Unsupported protocol type {scheme}."
                f"Available protocols: {avail_protocols}"
            )

        with self._cli_handler.get_cli_service(
            self._cli_handler.config_mode
        ) as config_session:
            save_action = SaveRestoreActions(config_session, self._logger)

            filename = url.get("filename", self.DEFAULT_CONFIG_NAME)
            save_action.save_configuration(filename=filename)

            if scheme in self.REMOTE_PROTOCOLS:
                with config_session.enter_mode(self._cli_handler.os_mode) as os_session:
                    system_action = SystemActions(os_session, self._logger)

                    hostname = url.get("hostname")
                    port = url.get("port")
                    path = url.get("path")
                    username = url.get("username")
                    password = url.get("password")

                    if scheme == "tftp":
                        system_action.tftp_put_file(
                            hostname=hostname,
                            port=port,
                            filename=filename,
                        )
                    elif scheme == "ftp":
                        system_action.ftp_put_file(
                            hostname=hostname,
                            port=port,
                            username=username,
                            password=password,
                            path=path,
                            filename=filename,
                        )
                    elif scheme == "scp":
                        if not path.endswith("/"):
                            path += "/"
                        system_action.scp_put_file(
                            hostname=hostname,
                            port=port,
                            username=username,
                            password=password,
                            path=path,
                            filename=filename,
                        )
                    system_action.os_delete_file(filename=filename)

    def _restore_flow(
        self, path, configuration_type, restore_method, vrf_management_name
    ):
        """Execute flow which save selected file to the provided destination.

        :param path: the path to the configuration file, including the configuration
            file name
        :param restore_method: the restore method to use when restoring the
            configuration file. Possible Values are append and override
        :param configuration_type: the configuration type to restore.
            Possible values are startup and running
        :param vrf_management_name: Virtual Routing and Forwarding Name
        """
        if not configuration_type.endswith("-config"):
            configuration_type += "-config"

        if configuration_type not in ["running-config"]:
            raise ExawareSaveRestoreException(
                "Device doesn't support saving '{}' configuration type".format(
                    configuration_type
                ),
            )

        if not restore_method:
            restore_method = "override"

        restore_method = self.RESTORE_TYPE_MAP[restore_method]

        url = UrlParser().parse_url(path)
        scheme = url.get("scheme")
        avail_protocols = self.REMOTE_PROTOCOLS + [self._file_system]
        if scheme not in avail_protocols:
            raise ExawareSaveRestoreException(
                f"Unsupported protocol type {scheme}."
                f"Available protocols: {avail_protocols}"
            )

        with self._cli_handler.get_cli_service(self._cli_handler.os_mode) as os_session:
            filename = url.get("filename", self.DEFAULT_CONFIG_NAME)
            system_action = SystemActions(os_session, self._logger)

            if scheme in self.REMOTE_PROTOCOLS:
                system_action = SystemActions(os_session, self._logger)

                hostname = url.get("hostname")
                port = url.get("port")
                path = url.get("path")
                username = url.get("username")
                password = url.get("password")

                if scheme == "tftp":
                    system_action.tftp_get_file(
                        hostname=hostname,
                        port=port,
                        filename=filename,
                    )
                elif scheme == "ftp":
                    system_action.ftp_get_file(
                        hostname=hostname,
                        port=port,
                        username=username,
                        password=password,
                        path=path,
                        filename=filename,
                    )
                elif scheme == "scp":
                    system_action.scp_get_file(
                        hostname=hostname,
                        port=port,
                        username=username,
                        password=password,
                        path=path,
                        filename=filename,
                    )
            with os_session.enter_mode(self._cli_handler.config_mode) as config_session:
                save_action = SaveRestoreActions(config_session, self._logger)
                save_action.load_configuration(
                    filename=filename, restore_type=restore_method
                )

            system_action.os_delete_file(filename=filename)

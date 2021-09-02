#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)

from cloudshell.networking.exaware.command_templates import system
from cloudshell.networking.exaware.helpers.exceptions import ExawareBaseException


class SystemActions(object):
    def __init__(self, cli_service, logger):
        """General System actions."""
        self._cli_service = cli_service
        self._logger = logger

    def commit(self):
        """Commit changes."""
        CommandTemplateExecutor(self._cli_service, system.COMMIT).execute_command()

    def top(self):
        """Exit to top level."""
        CommandTemplateExecutor(self._cli_service, system.TOP).execute_command()

    def os_delete_file(self, filename):
        output = CommandTemplateExecutor(
            self._cli_service, system.DELETE_FILE
        ).execute_command(filename=filename)

        if "cannot remove" in output:
            raise ExawareBaseException(f"Error during file removing: {output}")

    def tftp_get_file(self, hostname, port, filename):
        """Download file from remote server to device local storage."""
        CommandTemplateExecutor(
            self._cli_service, system.TFTP_GET_FILE
        ).execute_command(
            hostname=hostname,
            port=port,
            filename=filename,
        )

    def tftp_put_file(self, hostname, port, filename):
        """Upload file to remote server from device local storage."""
        CommandTemplateExecutor(
            self._cli_service, system.TFTP_PUT_FILE
        ).execute_command(
            hostname=hostname,
            port=port,
            filename=filename,
        )

        # Transfer timed out.

    def ftp_get_file(self, hostname, port, username, password, path, filename):
        """Download file from remote server to device local storage."""
        output = CommandTemplateExecutor(
            self._cli_service, system.FTP_GET_FILE
        ).execute_command(
            hostname=hostname,
            port=port,
            username=username,
            password=password,
            path=os.path.join(path, filename),
            filename=filename,
        )
        if "curl" in output:
            err_msg = output.split("curl")[-1]
            raise ExawareBaseException(f"Error during coping file: {err_msg}")

    def ftp_put_file(self, hostname, port, username, password, path, filename):
        """Upload file to remote server from device local storage."""
        output = CommandTemplateExecutor(
            self._cli_service, system.FTP_PUT_FILE
        ).execute_command(
            hostname=hostname,
            port=port,
            username=username,
            password=password,
            path=path,
            filename=filename,
        )
        if "curl" in output:
            err_msg = output.split("curl")[-1]
            raise ExawareBaseException(f"Error during coping file: {err_msg}")

    def scp_get_file(
        self,
        hostname,
        port,
        username,
        password,
        path,
        filename,
    ):
        """Download file from remote server to device local storage."""
        output = CommandTemplateExecutor(
            self._cli_service,
            system.SCP_GET_FILE,
            action_map=OrderedDict(
                {
                    r"[Pp]assword:": lambda session, logger: session.send_line(
                        password, logger
                    )
                }
            ),
        ).execute_command(
            hostname=hostname,
            port=port,
            username=username,
            path=os.path.join(path, filename),
            filename=filename,
        )
        if "scp" in output:
            err_msg = output.split("scp")[-1]
            raise ExawareBaseException(f"Error during coping file: {err_msg}")

    def scp_put_file(
        self,
        hostname,
        port,
        username,
        password,
        path,
        filename,
    ):
        """Upload file to remote server from device local storage."""
        output = CommandTemplateExecutor(
            self._cli_service,
            system.SCP_PUT_FILE,
            action_map=OrderedDict(
                {
                    r"[Pp]assword:": lambda session, logger: session.send_line(
                        password, logger
                    )
                }
            ),
        ).execute_command(
            hostname=hostname,
            port=port,
            username=username,
            path=path,
            filename=filename,
        )
        if "scp" in output:
            err_msg = output.split("scp")[-1]
            raise ExawareBaseException(f"Error during coping file: {err_msg}")

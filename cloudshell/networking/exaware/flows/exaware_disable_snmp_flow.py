#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.networking.exaware.command_actions.enable_disable_snmp_actions import (
    EnableDisableSnmpActions,
)
from cloudshell.networking.exaware.command_actions.system_actions import (
    SystemActions as SystemActions,
)
from cloudshell.networking.exaware.helpers.exceptions import ExawareSNMPException


class ExawareDisableSnmpFlow(object):
    def __init__(self, cli_handler, logger):
        """Disable SNMP flow."""
        self._cli_handler = cli_handler
        self._logger = logger

    def disable_flow(self, snmp_parameters):
        if "3" in snmp_parameters.version:
            message = "Device doesn't support SNMP v3."
            self._logger.error(message)
            raise ExawareSNMPException(message)
        elif not snmp_parameters.snmp_community:
            message = "SNMP community cannot be empty"
            self._logger.error(message)
            raise ExawareSNMPException(message)

        with self._cli_handler.get_cli_service(
            self._cli_handler.config_mode
        ) as conf_session:
            community = snmp_parameters.snmp_community
            snmp_actions = EnableDisableSnmpActions(conf_session, self._logger)
            system_actions = SystemActions(conf_session, self._logger)

            self._logger.info(f"Start removing SNMP communit {community}")
            snmp_actions.remove_snmp_comminity(community=community)
            # TODO Do we need to disable SNMP service at all?
            # system_actions.top()  # noqa: E800
            # snmp_actions.enable_snmp_service()  # noqa: E800
            system_actions.commit()

            self._logger.info(f"SNMP v2c community {community} removed")

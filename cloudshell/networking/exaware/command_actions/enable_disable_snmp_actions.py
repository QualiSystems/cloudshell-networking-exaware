#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)

from cloudshell.networking.exaware.command_templates import enable_disable_snmp
from cloudshell.networking.exaware.helpers.exceptions import ExawareSNMPException


class EnableDisableSnmpActions(object):
    def __init__(self, cli_service, logger):
        """Enable Disable Snmp actions."""
        self._cli_service = cli_service
        self._logger = logger

    def show_snmp_configuration(self):
        """Show SNMP configuration."""
        status = "disable"

        output = CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.SHOW_SNMP_CONFIGURATION
        ).execute_command()
        match = re.search(r"status\s+(?P<status>\w+)", output)
        if match:
            status = match.groupdict().get("status", "disable")

        communities = list(set(re.findall(r"community\s+(?P<community>\w+)", output)))

        return {"status": status, "communties": communities}

    def enable_snmp_service(self):
        """Enable SNMP agent and configure SNMP version."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.ENABLE_SNMP
        ).execute_command()

    def configure_snmp_community(self, community):
        """Configure SNMP v2c community."""
        output = CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.CONFIGURE_V2C_COMMUNITY
        ).execute_command(community=community)
        if "error" in output.lower():
            self._logger.error(
                "Configuration SNMP v2c community failed. {}".format(output)
            )
            raise ExawareSNMPException("Configuration SNMP v2c community failed")

    def remove_snmp_comminity(self, community):
        """Remove SNMP v2c community."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.REMOVE_V2C_COMMUNITY
        ).execute_command(community=community)

    def disable_snmp_service(self):
        """Disable SNMP service on the device."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.DISABLE_SNMP
        ).execute_command()

#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.snmp.snmp_configurator import (
    EnableDisableSnmpConfigurator,
    EnableDisableSnmpFlowInterface,
)

from cloudshell.networking.exaware.flows.exaware_disable_snmp_flow import ExawareDisableSnmpFlow
from cloudshell.networking.exaware.flows.exaware_enable_snmp_flow import ExawareEnableSnmpFlow


class ExawareEnableDisableSnmpFlow(EnableDisableSnmpFlowInterface):
    DEFAULT_SNMP_VIEW = "quali_snmp_view"
    DEFAULT_SNMP_GROUP = "quali_snmp_group"

    def __init__(self, cli_handler, logger):
        """Enable snmp flow."""
        self._logger = logger
        self._cli_handler = cli_handler

    def enable_snmp(self, snmp_parameters):
        ExawareEnableSnmpFlow(self._cli_handler, self._logger).enable_flow(
            snmp_parameters
        )

    def disable_snmp(self, snmp_parameters):
        ExawareDisableSnmpFlow(self._cli_handler, self._logger).disable_flow(
            snmp_parameters
        )


class ExawareSnmpHandler(EnableDisableSnmpConfigurator):
    def __init__(self, resource_config, logger, cli_handler):
        self.cli_handler = cli_handler
        enable_disable_snmp_flow = ExawareEnableDisableSnmpFlow(self.cli_handler, logger)
        super(ExawareSnmpHandler, self).__init__(
            enable_disable_snmp_flow, resource_config, logger
        )

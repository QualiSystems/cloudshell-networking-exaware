#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.snmp.snmp_parameters import SNMPWriteParameters  # noqa: F401

from cloudshell.networking.exaware.helpers.exceptions import (  # noqa: F401
    ExawareSNMPException,
)


class ExawareDisableSnmpFlow(object):
    def __init__(self, cli_handler, logger):
        """Disable SNMP flow."""
        self._cli_handler = cli_handler
        self._logger = logger

    def disable_flow(self, snmp_parameters):
        pass

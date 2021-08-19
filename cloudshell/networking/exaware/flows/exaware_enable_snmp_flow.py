#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.snmp.snmp_parameters import SNMPWriteParameters  # noqa: F401

from cloudshell.networking.exaware.helpers.exceptions import (  # noqa: F401
    ExawareSNMPException,
)


class ExawareEnableSnmpFlow(object):
    DEFAULT_SNMP_VIEW = "quali_snmp_view"
    DEFAULT_SNMP_GROUP = "quali_snmp_group"
    DEFAULT_SNMP_ACCESS = "read"
    ENCRYPTION = {
        "MD5": "md5",
        "SHA": "sha",
        "DES": "des56",
        "3DES-EDE": "3des",
        "AES-128": "aes128",
        "AES-192": "aes192",
        "AES-256": "aes256",
    }

    def __init__(self, cli_handler, logger):
        """Enable snmp flow."""
        self._logger = logger
        self._cli_handler = cli_handler

    def enable_flow(self, snmp_parameters):
        pass

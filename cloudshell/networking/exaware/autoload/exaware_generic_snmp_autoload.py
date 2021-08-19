#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.snmp.autoload.generic_snmp_autoload import (
    GenericSNMPAutoload,
)


class ExawareGenericSNMPAutoload(GenericSNMPAutoload):
    def __init__(self, snmp_handler, logger):
        super(ExawareGenericSNMPAutoload, self).__init__(snmp_handler, logger)

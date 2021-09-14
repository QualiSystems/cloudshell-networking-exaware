#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template import CommandTemplate

SHOW_SNMP_CONFIGURATION = CommandTemplate("show configuration running snmp")
ENABLE_SNMP = CommandTemplate("snmp status enable")
DISABLE_SNMP = CommandTemplate("snmp status disable")
CONFIGURE_V2C_COMMUNITY = CommandTemplate("snmp community {community}")
REMOVE_V2C_COMMUNITY = CommandTemplate("no snmp community {community}")

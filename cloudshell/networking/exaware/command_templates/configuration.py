# !/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template import CommandTemplate

SAVE_CONFIG = CommandTemplate("save {filename}")
LOAD_CONFIG = CommandTemplate("load {restore_type} {filename}")
DELETE_CONFIG = CommandTemplate("file delete {filename}")

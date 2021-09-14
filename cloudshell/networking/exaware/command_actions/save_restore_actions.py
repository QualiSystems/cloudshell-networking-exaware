#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)

from cloudshell.networking.exaware.command_templates import configuration
from cloudshell.networking.exaware.helpers.exceptions import ExawareSaveRestoreException


class SaveRestoreActions(object):
    def __init__(self, cli_service, logger):
        """Save and Restore actions."""
        self._cli_service = cli_service
        self._logger = logger

    def save_configuration(self, filename):
        """Save configuration to file."""
        CommandTemplateExecutor(
            self._cli_service, configuration.SAVE_CONFIG
        ).execute_command(filename=filename)

    def load_configuration(self, filename, restore_type):
        """Load configuration from file."""
        output = CommandTemplateExecutor(
            self._cli_service, configuration.LOAD_CONFIG
        ).execute_command(filename=filename, restore_type=restore_type)

        if "Operation completed successfully" not in output:
            raise ExawareSaveRestoreException(f"Failed to load configuration: {output}")

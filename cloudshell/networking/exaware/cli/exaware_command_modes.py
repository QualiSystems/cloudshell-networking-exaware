#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.service.command_mode import CommandMode


class OperationCommandMode(CommandMode):
    PROMPT = r"\S+(?!\)).#"
    ENTER_COMMAND = ""
    EXIT_COMMAND = "exit"

    def __init__(self, resource_config):
        """Initialize Operation command mode."""
        self.resource_config = resource_config

        super(OperationCommandMode, self).__init__(
            prompt=self.PROMPT,
            enter_command=self.ENTER_COMMAND,
            exit_command=self.EXIT_COMMAND,
        )


class ConfigurationCommandMode(CommandMode):
    PROMPT = r"\S+\(config(\S)*\)#"
    ENTER_COMMAND = "configure"
    EXIT_COMMAND = "exit"

    def __init__(self, resource_config):
        """Initialize Configuration command mode."""
        self.resource_config = resource_config

        super(ConfigurationCommandMode, self).__init__(
            prompt=self.PROMPT,
            enter_command=self.ENTER_COMMAND,
            exit_command=self.EXIT_COMMAND,
        )


class OSShellCommandMode(CommandMode):
    PROMPT = r"\w+@\S+\[CPM-0-0_A\]:~\$"
    ENTER_COMMAND = "os-shell"
    EXIT_COMMAND = "exit"

    def __init__(self, resource_config):
        """Initialize OS Shell command mode."""
        self.resource_config = resource_config

        super(OSShellCommandMode, self).__init__(
            prompt=self.PROMPT,
            enter_command=self.ENTER_COMMAND,
            exit_command=self.EXIT_COMMAND,
        )


CommandMode.RELATIONS_DICT = {
    OperationCommandMode: {
        ConfigurationCommandMode: {},
        OSShellCommandMode: {}
    }
}

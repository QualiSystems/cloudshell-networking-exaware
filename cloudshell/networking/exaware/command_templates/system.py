# !/usr/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate

COMMIT = CommandTemplate("commit")
TOP = CommandTemplate("top")

DELETE_FILE = CommandTemplate("rm {filename}")

TFTP_GET_FILE = CommandTemplate("tftp {hostname}[ {port}] -c get {filename}")
TFTP_PUT_FILE = CommandTemplate("tftp {hostname}[ {port}] -c put {filename}")

FTP_GET_FILE = CommandTemplate(
    "curl [-u {username}][:{password}] -o {filename} ftp://{hostname}[:{port}]/{path}"
)
FTP_PUT_FILE = CommandTemplate(
    "curl [-u {username}][:{password}] -T {filename} ftp://{hostname}[:{port}]/{path}"
)

SCP_ACTION_MAP = OrderedDict(
    # {r"Are you sure you want to continue connecting \(yes\/no\)\?"
    {r"\(yes\/no\)\?": lambda session, logger: session.send_line("yes", logger)}
)
SCP_GET_FILE = CommandTemplate(
    "scp [-P {port}] {username}@{hostname}:{path} {filename}",
    action_map=SCP_ACTION_MAP,
)
SCP_PUT_FILE = CommandTemplate(
    "scp [-P {port}] {filename} {username}@{hostname}:{path}",
    action_map=SCP_ACTION_MAP,
)

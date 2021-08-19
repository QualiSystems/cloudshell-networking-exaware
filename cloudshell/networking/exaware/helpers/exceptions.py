#!/usr/bin/python
# -*- coding: utf-8 -*-


class ExawareBaseException(Exception):
    """Base Exaware exception."""


class ExawareSNMPException(ExawareBaseException):
    """Exaware enable/disable SNMP configuration exception."""


class ExawareSaveRestoreException(ExawareBaseException):
    """Exaware save/restore configuration exception."""


class ExawareConnectivityException(ExawareBaseException):
    """Exaware connectivity exception."""


class ExawareFirmwareException(ExawareBaseException):
    """Exaware load firmware exception."""

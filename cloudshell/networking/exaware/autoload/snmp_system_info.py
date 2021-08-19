#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

from cloudshell.snmp.autoload.snmp_system_info import SnmpSystemInfo


class ExawareSnmpSystemInfo(SnmpSystemInfo):
    SYS_DESCR_PATTERN = re.compile(r"\S+\s+(?P<model>\S+)\s+(?P<os_version>\S+:\S+)$")

    def __init__(self, snmp_handler, logger, vendor=None):
        super(ExawareSnmpSystemInfo, self).__init__(snmp_handler, logger, vendor)

    def _get_vendor(self):
        """Get device vendor."""
        return "Exaware"

    def _get_device_model(self):
        """Get device model."""
        result = ""
        matched = re.search(
            self.SYS_DESCR_PATTERN, str(self._snmp_v2_obj.get_system_description())
        )
        if matched:
            result = matched.groupdict().get("model", "")
        return result

    def _get_device_os_version(self):
        """Get device OS Version."""
        result = ""
        matched = re.search(
            self.SYS_DESCR_PATTERN, str(self._snmp_v2_obj.get_system_description())
        )
        if matched:
            result = matched.groupdict().get("os_version", "")
        return result

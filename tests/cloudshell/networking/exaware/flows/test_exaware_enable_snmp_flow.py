#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase

from cloudshell.networking.exaware.flows.exaware_enable_snmp_flow import (
    ExawareEnableSnmpFlow,
)


class TestExawareEnableSnmpFlow(TestCase):
    def test_import(self):
        self.assertTrue(ExawareEnableSnmpFlow)

#!/usr/bin/env python3
#
# run tests of the grpkg command and subcommands
#

import os
import re
import subprocess
import sys
import unittest

ROOTNAME = "grpkg"


def run_cmd(cmd):
    env = os.environ.copy()
    env["PATH"] = env["PATH"] + os.pathsep + "."
    res = subprocess.run(cmd, env=env, 
                         capture_output=True, text=True, check=True)
    return res

class TestTestArgs(unittest.TestCase):
    """
    These tests are for command lines of the form: grpkg test --option
    """
    
    DEFAULT_TEXT = """grpkg test: default: list all the possible test cases
"""

    DESCRIPTION = """grpkg test: run a simple test case
"""

    HELP = """usage: grpkg test {<case>|-v|--version}

where:
   <case>          name of the test case

global options are:
   -d|--description    display one line description
   -D|--debug          display some debug messages
   -h|--help           display this message
   -v|--verbose        be noisy whilst busy
   -V|--version        display version numbers for all known components
"""

    VERSION = """grpkg test: v20250512-1
"""

    def test_noargs(self):
        res = run_cmd([ROOTNAME, "test"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.DEFAULT_TEXT)

    def test_d_arg(self):
        res = run_cmd([ROOTNAME, "test", "-d"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.DESCRIPTION)

    def test_D_arg(self):
        res = run_cmd([ROOTNAME, "test", "-D"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.DEFAULT_TEXT)

    def test_debug_arg(self):
        res = run_cmd([ROOTNAME, "test", "--debug"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.DEFAULT_TEXT)

    def test_description_arg(self):
        res = run_cmd([ROOTNAME, "test", "--description"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.DESCRIPTION)

    def test_h_arg(self):
        res = run_cmd([ROOTNAME, "test", "-h"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.HELP)

    def test_help_arg(self):
        res = run_cmd([ROOTNAME, "test", "--help"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.HELP)

    def test_v_arg(self):
        res = run_cmd([ROOTNAME, "test", "-v"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.DEFAULT_TEXT)

    def test_V_arg(self):
        res = run_cmd([ROOTNAME, "test", "-V"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.VERSION)

    def test_verbose_arg(self):
        res = run_cmd([ROOTNAME, "test", "--verbose"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.DEFAULT_TEXT)

    def test_version(self):
        res = run_cmd([ROOTNAME, "test", "--version"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestTestArgs.VERSION)


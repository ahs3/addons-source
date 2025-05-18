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

class TestGlobalArgs(unittest.TestCase):
    """
    These tests are for command lines of the form: grpkg --option
    """

    DEFAULT_TEXT="""main: do the default
"""
    DESCRIPTION="""grpkg: tools to help develop and package Gramps addons
"""

    VERSION="""grpkg v0.0.1, SPDX-License-Identifier: GPL-2.0

Command versions:
    init         v0.0.1 
    test         v20250512-1 
"""

    HELP="""usage: grpkg { <command> [<option>...] | [<global-option>...] }

global options are:
   -d|--description    display one line description
   -D|--debug          display some debug messages
   -h|--help           display this message
   -v|--verbose        be noisy whilst busy
   -V|--version        display version numbers for all known components

Tools for Gramps addon development

Known subcommands:
   init         initialize a development directory for a Gramps addon
   test         run a simple test case

Use grpkg <subcommand> --help for command specific information
"""

    def test_noargs(self):
        res = run_cmd(ROOTNAME)
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.DEFAULT_TEXT)

    def test_d_arg(self):
        res = run_cmd([ROOTNAME, "-d"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.DESCRIPTION)

    def test_D_arg(self):
        res = run_cmd([ROOTNAME, "-D"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.DEFAULT_TEXT)

    def test_debug_arg(self):
        res = run_cmd([ROOTNAME, "--debug"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.DEFAULT_TEXT)

    def test_description_arg(self):
        res = run_cmd([ROOTNAME, "--description"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.DESCRIPTION)

    def test_h_arg(self):
        res = run_cmd([ROOTNAME, "-h"])
        self.maxDiff = None
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.HELP)

    def test_help_arg(self):
        res = run_cmd([ROOTNAME, "--help"])
        self.maxDiff = None
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.HELP)

    def test_v_arg(self):
        res = run_cmd([ROOTNAME, "-v"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.DEFAULT_TEXT)

    def test_V_arg(self):
        res = run_cmd([ROOTNAME, "-V"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.VERSION)

    def test_verbose_arg(self):
        res = run_cmd([ROOTNAME, "--verbose"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.DEFAULT_TEXT)

    def test_version(self):
        res = run_cmd([ROOTNAME, "--version"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestGlobalArgs.VERSION)



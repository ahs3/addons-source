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

class TestInitArgs(unittest.TestCase):
    """
    These tests are for command lines of the form: grpkg test --option
    """
    
    NOARGS_TEXT = """? a directory name is required
usage: grpkg init <name>
where:
   <name>       Python module name to use for the addon
                (use camel case, please)
"""

    DEFAULT_TEXT = "main: do the default\n" + NOARGS_TEXT

    DESCRIPTION = """grpkg init: initialize a development directory for a Gramps addon
""" + NOARGS_TEXT

    VERSION = """grpkg init: v0.0.1
"""

    def test_noargs(self):
        """
        A directory name is required, so noargs is a failure
        """
        res = run_cmd([ROOTNAME, "init"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestInitArgs.NOARGS_TEXT)

    def test_d_arg(self):
        res = run_cmd([ROOTNAME, "init", "-d"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestInitArgs.DESCRIPTION)

    def test_D_arg(self):
        res = run_cmd([ROOTNAME, "init", "-D"])
        self.assertTrue(len(res.stdout)>0)
        stdout = re.sub(r"^INIT>.*\n", "", res.stdout)
        self.assertEqual(stdout, TestInitArgs.NOARGS_TEXT)

    def test_debug_arg(self):
        res = run_cmd([ROOTNAME, "init", "--debug"])
        self.assertTrue(len(res.stdout)>0)
        stdout = re.sub(r"^INIT>.*\n", "", res.stdout)
        self.assertEqual(stdout, TestInitArgs.NOARGS_TEXT)

    def test_description_arg(self):
        res = run_cmd([ROOTNAME, "init", "--description"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestInitArgs.DESCRIPTION)

    def test_v_arg(self):
        res = run_cmd([ROOTNAME, "init", "-v"])
        self.assertTrue(len(res.stdout)>0)
        stdout = re.sub(r"^INIT>.*\n", "", res.stdout)
        self.assertEqual(stdout, TestInitArgs.NOARGS_TEXT)

    def test_V_arg(self):
        res = run_cmd([ROOTNAME, "init", "-V"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestInitArgs.VERSION)

    def test_verbose_arg(self):
        res = run_cmd([ROOTNAME, "init", "--verbose"])
        self.assertTrue(len(res.stdout)>0)
        stdout = re.sub(r"^INIT>.*\n", "", res.stdout)
        self.assertEqual(stdout, TestInitArgs.NOARGS_TEXT)

    def test_version(self):
        res = run_cmd([ROOTNAME, "init", "--version"])
        self.assertTrue(len(res.stdout)>0)
        self.assertEqual(res.stdout, TestInitArgs.VERSION)


if __name__ == "__main__":
    unittest.main()

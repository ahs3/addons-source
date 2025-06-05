#!/usr/bin/env python3
#
#	Utilities for grpkg command
#
# Copyright 2025, Al Stone <ahs3@ahs3.net>, All Rights Reserved.
# SPDX-License-Identifier: GPL-2.0
#

import argparse
import configparser
import glob
import os
import subprocess
import sys

CONFIG_FILE_NAME = "grpkg.ini"
ROOTNAME = "grpkg"

extended_env = {}
subcommands = {}

def extend_path():
    global extended_env

    if not extended_env:
        extended_env = os.environ.copy()
        if extended_env["PATH"].find("."+os.pathsep) == -1 and \
           extended_env["PATH"].find(os.pathsep+".") == -1:
            extended_env["PATH"] = extended_env["PATH"] + os.pathsep + "."
    return extended_env

def fixpath(p):
    return os.path.expanduser(os.path.expandvars(p))

def findem(pat=ROOTNAME):
    global subcommands

    if len(subcommands) == 0:
        cmds = {}
        dirs = os.environ["PATH"].split(":")
        if ":" not in dirs:
            dirs.append(".")
        for ii in dirs:
            p = os.path.join(ii, ROOTNAME+"-*")
            found = glob.glob(p)
            for jj in found:
                fp = fixpath(jj)
                base = os.path.basename(fp)
                if base in cmds:
                    continue
                if os.path.isfile(fp) and os.access(fp, os.X_OK):
                    cmds[base] = {"sub": base.split("-")[1],
                                  "path":fp,
                                  "desc": "",
                                 }
            subcommands = dict(sorted(cmds.items()))
    return subcommands

def find_subcommand(sub=None):
    global subcommands

    res = None
    if sub:
        for ii in subcommands:
            if subcommands[ii]["sub"] == sub:
                res = ii
                break
    return res

def is_subcommand(cmd):
    return ROOTNAME+"-"+cmd in subcommands

def print_global_args():
    print(f"\nglobal options are:")
    print(f"   -d|--description    display one line description")
    print(f"   -D|--debug          display some debug messages")
    print(f"   -h|--help           display this message")
    print(f"   -v|--verbose        be noisy whilst busy")
    print(f"   -V|--version        display version numbers for all known components")
 
class UsageAction(argparse.Action):
    def __init__(self,
                 option_strings,
                 subcommand,            # my addition
                 dest=None,
                 nargs=0,
                 default=None,
                 required=False,
                 type=None,
                 metavar=None,
                 help=None):
        self.subcommand = subcommand
        super(UsageAction, self).__init__(
                option_strings=option_strings,
                dest=dest,
                nargs=nargs,
                default=default,
                required=required,
                metavar=metavar,
                type=type,
                help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        global subcommands

        setattr(namespace, self.dest, values)

        print(f"usage: {ROOTNAME} {{ <command> [<option>...] | [<global-option>...] }}")
        print_global_args()
 
        print(f"\n{parser.description}")
        print("\nKnown subcommands:")
        for ii in subcommands:
            sub = subcommands[ii]["sub"]
            desc = subcommands[ii]["desc"]
            print(f"   {sub:10s}   {desc}")
        print(f"\n{parser.epilog}")
        sys.exit(0)

class Args:
    def __init__(self):
        global subcommands

        setattr(Args, "help", False)
        setattr(Args, "subcommand", None)
        for ii in sys.argv[1:]:
            if ii[0] != "-":
                Args.subcommand = ii
                break
        self.parser = argparse.ArgumentParser(
                            prog=ROOTNAME,
                            usage=f"{ROOTNAME} [<subcommand>] [<option>...]",
                            description="Tools for Gramps addon development",
                            epilog=f"Use {ROOTNAME} <subcommand> --help for command specific information",
                            exit_on_error=False,
                            add_help=False,
                      )
        self.parser.add_argument("-d", "--description", action="store_true",
                                 help=f"display command description",
                                 default=False,
                                )
        self.parser.add_argument("-D", "--debug", action="store_true",
                                 help=f"enable debug messages to stderr",
                                 default=False,
                                )
        self.parser.add_argument("-h", "--help",
                                 help=f"display this message",
                                 default=False,
                                 action=UsageAction,
                                 subcommand=Args.subcommand,
                                )
        self.parser.add_argument("-v", "--verbose", action="store_true",
                                 help=f"enable verbose messages to stdout",
                                 default=False,
                                )
        self.parser.add_argument("-V", "--version", action="store_true",
                                 help=f"display version information",
                                 default=False,
                                )
        
        self.subparsers = self.parser.add_subparsers(
                                title="subcommands",
                                description="known subcommands",
                          )
        subcommands = findem()
        for ii in subcommands:
            cmd = [ii, "--description"]
            env = extend_path()
            res = subprocess.run(cmd, env=env, capture_output=True, text=True)
            help_fields = res.stdout.split(":")
            help_text = help_fields[1].strip()
            subcommands[ii]["desc"] = help_text
            parser = self.subparsers.add_parser(subcommands[ii]["sub"],
                                                help=help_text,
                                                add_help=False,
                                               )
        try:
            self.namespace, self.unknowns = self.parser.parse_known_args()
            for name, value in vars(self.namespace).items():
                setattr(Args, name, value)
        except argparse.ArgumentError as ae:
            fields = str(ae).split(":")
            if fields[0].strip() == "unrecognized arguments":
                print(f"? no such option: {fields[1].strip()}")
            elif fields[1].strip() == "invalid choice":
                print(f"? no such subcommand: {fields[2].strip()}")
            print(fields)
            sys.exit(1)

    def print_help(self):
        self.parser.print_help()


class GrConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file_name = ""
        home_config = os.path.join(os.path.join(os.environ["HOME"],
                                                ".config",
                                                ROOTNAME,
                                                CONFIG_FILE_NAME))

        if os.path.exists(CONFIG_FILE_NAME):
            self.config.read(CONFIG_FILE_NAME)
            self.file_name = CONFIG_FILE_NAME
        elif os.path.exists(home_config):
            self.config.read(home_config)
            self.file_name = home_config
        else:
            os.makedirs(os.path.dirname(home_config), exist_ok=True)
            gpath = os.path.normpath(os.path.join(os.environ["PWD"],
                                                  "..",
                                                  "gramps"
                                                 )
                                    )
            self.config["DEFAULT"] = { "user": os.environ["USER"],
                                       "workspace": os.environ["PWD"],
                                       "language": os.environ["LANG"],
                                       "grampspath": gpath,
                                     }
            self.file_name = home_config

    def get(self, section, item):
        res = None
        if section in self.config:
            if item in self.config[section]:
                res = self.config[section][item]
        return res

    def put(self, section, item, value):
        if section in self.config:
            if item in self.config[section]:
                self.config[section][item] = str(value)
        else:
            self.config[section][item] = str(value)
        return

    def close(self):
        print("got here")
        with open(self.file_name, "w+") as cfd:
            self.config.write(cfd)


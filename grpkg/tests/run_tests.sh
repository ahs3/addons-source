#!/bin/bash
#
#	run the test suite
#

SOURCEDIR="../"
export PATH=$PATH:$SOURCEDIR

./grtests $*

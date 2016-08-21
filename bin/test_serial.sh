#!/bin/bash
#
# Title:test_serial.sh
# Description:exercise BC785 on serial port
# Development Environment:OS X 10.10.5
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ROOT_DIR=/home/gsc/github/mellow-elephant-py; export ROOT_DIR
#
PYTHONPATH=$ROOT_DIR/src/main/python/mellow_elephant; export PYTHONPATH
#
$ROOT_DIR/src/main/python/mellow_elephant/bc780_test.py $ROOT_DIR/bin/test.yaml
#

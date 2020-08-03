#!/bin/bash
#
# Title:test_usb0.sh
# Description:test to ensure receiver is working
# Development Environment:OS X 10.10.5
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ROOT_DIR=/home/gsc/github/mellow-elephant; export ROOT_DIR
#
source $ROOT_DIR/src/venv/bin/activate
#
python3 $ROOT_DIR/src/serial_test.py $ROOT_DIR/bin/serial_test.yaml
#

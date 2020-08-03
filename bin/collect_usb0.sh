#!/bin/bash
#
# Title:collect_usb0.sh
# Description:perform collection w/BC780 on USB0
# Development Environment:OS X 10.10.5
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ROOT_DIR=/home/gsc/github/mellow-elephant; export ROOT_DIR
#
source $ROOT_DIR/src/venv/bin/activate
#
python3 $ROOT_DIR/src/collection.py $ROOT_DIR/bin/collect.yaml
#
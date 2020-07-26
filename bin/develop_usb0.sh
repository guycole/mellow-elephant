#!/bin/bash
#
# Title:develop_usb0.sh
# Description:develop w/BC785 on USB0
# Development Environment:OS X 10.10.5
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ROOT_DIR=/home/gsc/github/mellow-elephant; export ROOT_DIR
#
source $ROOT_DIR/src/venv/bin/activate
#
python3 $ROOT_DIR/src/collection/collection.py $ROOT_DIR/bin/develop.yaml
#

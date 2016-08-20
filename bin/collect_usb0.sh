#!/bin/bash
#
# Title:collect_usb0.sh
# Description:perform collection w/BC785 on USB0
# Development Environment:OS X 10.10.5
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ROOT_DIR=/Users/gsc/IdeaProjects/mellow-elephant-py; export ROOT_DIR
#
PYTHONPATH=$ROOT_DIR/src/main/python/mellow_elephant; export PYTHONPATH
#
/usr/bin/logger -i -p local3.info collect usb0 start
#
$ROOT_DIR/src/main/python/mellow_elephant/collection.py $ROOT_DIR/bin/config_usb0.yaml
#
/usr/bin/logger -i -p local3.info collect usb0 stop
#

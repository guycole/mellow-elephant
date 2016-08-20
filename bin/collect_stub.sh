#!/bin/bash
#
# Title:collect_stub.sh
# Description:simulated receiver
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
$ROOT_DIR/src/main/python/mellow_elephant/collection.py $ROOT_DIR/bin/config_stub.yaml
#
/usr/bin/logger -i -p local3.info collect usb0 stop
#

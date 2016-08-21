#!/bin/bash
#
# Title:plot.sh
# Description:make band plot
# Development Environment:OS X 10.10.5
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ROOT_DIR=/Users/gsc/IdeaProjects/mellow-elephant-py; export ROOT_DIR
#
PYTHONPATH=$ROOT_DIR/src/main/python/mellow_elephant; export PYTHONPATH
#
/usr/bin/logger -i -p local3.info process start
#
$ROOT_DIR/src/main/python/mellow_elephant/processing.py $ROOT_DIR/bin/process.yaml
#
/usr/bin/logger -i -p local3.info process stop
#

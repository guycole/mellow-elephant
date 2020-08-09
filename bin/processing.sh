#!/bin/bash
#
# Title:processing.sh
# Description:process collected json band files
# Development Environment:OS X 10.10.5
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ROOT_DIR=/home/gsc/github/mellow-elephant; export ROOT_DIR
ROOT_DIR=/Users/gsc/IdeaProjects/mellow-elephant; export ROOT_DIR
#
source $ROOT_DIR/src/venv/bin/activate
#
python3 $ROOT_DIR/src/processing.py $ROOT_DIR/bin/processing.yaml
#
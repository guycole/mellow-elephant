#!/bin/bash
#
# Title:converter.sh
#
# Description:
#   Convert sorties from mysql to python pickle
#
# Development Environment:
#   OS X 10.10.5
#
# Author:
#   G.S. Cole (guycole at gmail dot com)
#
# Maintenance History:
#   $Id$
#
#   $Log$
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
PYTHONPATH=/mnt/disk1/gsc/git/mellow-elephant-py; export PYTHONPATH
#
/mnt/disk1/gsc/git/mellow-elephant-py/migrator/converter.py /var/mellow/elephant/config.yaml
#

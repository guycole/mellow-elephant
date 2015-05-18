#
# Title:collection.py
# Description:Mellow Elephant collection
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import sys

import yaml

from Task import Task

class Collector:

    def execute(self, task, runMode):
        print "runMode:%s" % runMode

        if runMode == 'once':
            task.execute()
        elif runMode == 'always':
            while True:
                task.execute()
        else:
            print "unsupported run mode:%s" % runMode

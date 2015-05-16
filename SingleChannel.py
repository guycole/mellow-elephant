#! /usr/bin/python
#
# Title:SingleChannel.py
# Description:command the scanner to visit a single frequency
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import sys
import yaml

import PidLock

class SingleChannel:

    def execute(self):
        print 'hit'

print 'start driver'

#
# argv[1] = frequency in MHz, i.e. 123.45
# argv[2] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        frequency = sys.argv[1]
    else:
        print 'must supply frequency'
        sys.exit(-1)

    if len(sys.argv) > 2:
        yamlFileName = sys.argv[1]
    else:
        yamlFileName = 'config.yaml'

    configuration = yaml.load(file(yamlFileName))

    loaderLockFile = configuration['loaderLockFile']

    pidLock = PidLock.PidLock()
    if pidLock.lockTest(loaderLockFile):
        print 'pid lock active'
    else:
        print 'fresh pid lock'

        pidLock.writeLock(loaderLockFile)

# driver = QueueDriver()
#        driver.execute(taskId, sqlWrapper, queue)

print 'stop driver'

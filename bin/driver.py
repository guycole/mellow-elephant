#! /usr/bin/python
#
# Title:driver.py
# Description:
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import sys
import yaml

#from mellow_elephant_core import collector
from mellow_elephant_core import receiver
from mellow_elephant_core import task

print 'start'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        fileName = "config.yaml"

    configuration = yaml.load(file(fileName))

    dataDirectory = configuration['dataDirectory']
    print dataDirectory

    installationId = configuration['installationId']
    print installationId

    receiverType = configuration['receiverType']
    receiverProxy = configuration['receiverProxy']

    receiverFactory = receiver.ReceiverFactory()
    receiver = receiverFactory.factory(receiverType, receiverProxy)

    task2 = task.Task(configuration['frequencyBands'], receiver, installationId, dataDirectory)

    pidLockPath = configuration['pidLockPath']
    print pidLockPath

    task2.execute()

#    pidFile = "%s/Collector" % pidLockPath
#    pidLock = PidLock()
#    if pidLock.lockTest(pidFile):
#        print 'pid lock noted'
#    else:
#        print 'pid lock fail'
#        pidLock.writeLock(pidFile)
#
#        collector = Collector()
#        collector.execute(task, configuration['runMode'])

print 'stop'

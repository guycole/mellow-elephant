#! /usr/bin/python
#
# Title:collection.py
# Description:
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import sys
import yaml

#from mellow_elephant_core import collector
from mellow_elephant_core import pid_lock
from mellow_elephant_core import receiver
from mellow_elephant_core import task

def execute(frequencyBands, receiver, dataDirectory):
    currentTask = task.Task(frequencyBands, receiver, dataDirectory)
    currentTask.execute()

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

    receiverType = configuration['receiverType']
    receiverProxy = configuration['receiverProxy']

    receiverFactory = receiver.ReceiverFactory()
    receiver = receiverFactory.factory(receiverType, receiverProxy)

    pidLockPath = configuration['pidLockPath']
    print pidLockPath

    pidFile = "%s/collection" % pidLockPath
    pidLock = pid_lock.PidLock()
    if pidLock.lockTest(pidFile):
        print 'pid lock noted'
    else:
        print 'pid lock fail'
        pidLock.writeLock(pidFile)
        execute(configuration['frequencyBands'], receiver, dataDirectory)

print 'stop'

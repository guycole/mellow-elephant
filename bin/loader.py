#! /usr/bin/python
#
# Title:loader.py
# Description:
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import pickle
import sys
import yaml

from mellow_elephant_core import discovery
from mellow_elephant_core import uploader

print 'start'

def execute(dataDirectory):
    discoverer = discovery.Discovery()
    sortieFiles = discoverer.discoverSorties(dataDirectory)
    for sortieFile in sortieFiles:
        observationFiles = discoverer.discoverObservations(sortieFile)
        for observationFile in observationFiles:
            print observationFile
            observationList = pickle.load(open(observationFile, "rb"))
            for observation in observationList:
                print observation

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

    pidLockPath = configuration['pidLockPath']
    print pidLockPath

    execute(dataDirectory)

##################

#    currentTask.execute()

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

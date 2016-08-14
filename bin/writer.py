#! /usr/bin/python
#
# Title:writer.py
# Description:
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import datetime
import os
import pickle
import sys
import yaml

from mellow_elephant_core import discovery

from boto.s3.connection import S3Connection
from boto.s3.key import Key

print 'start'

def uploadObservation(fileName):
    print 'xxx'
    print fileName

    observationRows = pickle.load(open(fileName, "rb"))
    print len(observationRows)

    bandNdx = observationRows[0].band
    obsTime = datetime.datetime.utcfromtimestamp(observationRows[0].timeStampMs/1000)
    print bandNdx
    print obsTime

    timeBuffer = obsTime.timetuple()

    s3directory = "elephant/elephant-%4.4d-%2.2d" % (timeBuffer[0], timeBuffer[1])
    print s3directory

    s3fileName = "%4.4d_%2.2d_%2.2d_%2.2d_%2.2d_b%2.2d" % (timeBuffer[0], timeBuffer[1], timeBuffer[2], timeBuffer[3], timeBuffer[4], bandNdx)
    print s3fileName

    command = "/bin/cp %s /tmp/%s" % (fileName, s3fileName)
    print command
    os.system(command)

    command = "/opt/local/bin/gzip -f /tmp/%s" % (s3fileName)
    print command
    os.system(command)

    s3connection = S3Connection()
    s3bucket = s3connection.get_bucket('mellow-digiburo-com')

    keyName = "%s/%s.gz" % (s3directory, s3fileName)
    targetName = "/tmp/%s.gz" % (s3fileName)

    statInfo = os.stat(targetName)

    s3key = Key(s3bucket)
    s3key.key = keyName
    count = s3key.set_contents_from_filename(targetName)

    os.unlink(targetName)

    if (count == statInfo.st_size):
        print 'size match'
        return True
    else:
        print 'size fail'
        return False

def execute(dataDirectory):
    os.chdir(dataDirectory)

    discoverer = discovery.Discovery()

    # complete sortie directories contain a sortie.p file
    sortieDirectories = discoverer.discoverSorties(dataDirectory)
    print "sortieDirectory size:%d" % len(sortieDirectories)
    for sortieDirectory in sortieDirectories:
        print sortieDirectory

        observationFiles = discoverer.discoverObservations(sortieDirectory)
        for observationFile in observationFiles:
            if observationFile.endswith('sortie.p'):
                print 'skipping sortie.p'
            else:
                flag = uploadObservation(observationFile)
                if (flag is True):
                    os.unlink(observationFile)
                else:
                    print "skipping failure:%s" % observationFile
                    return

        command = "/bin/rm -rf %s" % sortieDirectory
        print command
        os.system(command)

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

print 'stop'

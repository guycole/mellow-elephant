#! /usr/bin/python
#
# Title:Collector.py
# Description:Mellow Elephant collector parent
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import sys
import yaml

from ReceiverFactory import ReceiverFactory

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

	homeUrl = configuration['homeUrl']
	print homeUrl

	receiverType = configuration['receiverType']
	receiverProxy = configuration['receiverProxy']

	receiverFactory = ReceiverFactory()
	receiver = receiverFactory.factory(receiverType, receiverProxy)

	task = Task(configuration['frequencyBands'], receiver, installationId, dataDirectory, homeUrl)

	collector = Collector()
	collector.execute(task, configuration['runMode'])

print 'stop'

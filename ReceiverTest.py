#
# Title:ReceiverTest.py
# Description:stub receiver
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
from Receiver import Receiver

class ReceiverTest(Receiver):
	def __init__(self):
		Receiver.__init__(self, 'testRx', 'testPort')
		print 'receiver test ctor'
		print self.serialPort

	def getNextObservation(self):
		frequency = 123
		sample = 123

		observed = Observation(frequency, sample)
		return observed
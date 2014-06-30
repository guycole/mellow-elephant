#
# Title:Receiver.py
# Description:radio receiver parent
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
from Observation import Observation

class Receiver:
	def __init__(self, receiverType, serialPort):
		print 'receiver ctor'
		self.receiverType = receiverType
		self.serialPort = serialPort
		self.frequency = 1

	def __str__(self):
		return self.receiverType

	def openPort(self):
		print 'open port'

	def getNextObservation(self):
		frequency = 123
		sample = 123

		observed = Observation(frequency, sample)
		return observed

############################

	def getNextFrequency(self):
		result = self.frequency
		self.frequency += 1
		return result

	def observation(self, frequency):
		print 'observation %d' % frequency

		sample = 123

		observed = Observation(frequency, sample)
		return observed
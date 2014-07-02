#
# Title:Receiver.py
# Description:radio receiver parent
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

class Receiver:
	def __init__(self, receiverType, serialPort):
		print 'receiver ctor'
		self.receiverType = receiverType
		self.serialPort = serialPort

	def __str__(self):
		return self.receiverType

	def openPort(self):
		print 'open port'

	def sampleBand(self, band):
		print 'sample band:%f %f' % (band.frequencyLow, band.frequencyHigh)

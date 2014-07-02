#
# Title:Bc780.py
# Description:observation container
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
from Observation import Observation
from Receiver import Receiver

class ReceiverBc780(Receiver):
	def __init__(self, serialPort):
		Receiver.__init__(self, 'bc780', serialPort)
		print 'rx bc780 ctor'

	def sampleFrequency(self, frequency):
		print 'sample frequency:%d' % frequency
		return(Observation(frequency, 123))

	def sampleBand(self, band):
		print 'sample band:%f %f' % (band.frequencyLow, band.frequencyHigh)

		lowFreq = int(band.frequencyLow * 10000)
		highFreq = int(band.frequencyHigh * 10000)
		stepFreq = int(band.frequencyStep * 10)

		print 'sample band:%d %d' % (lowFreq, highFreq)

		resultList = []
		currentFrequency = lowFreq
		while currentFrequency < highFreq:
			resultList.append(self.sampleFrequency(currentFrequency))
			currentFrequency += stepFreq

		return(resultList)

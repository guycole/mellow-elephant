#
# Title:Bc780.py
# Description:observation container
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import time

from Observation import Observation
from Receiver import Receiver

class ReceiverBc780(Receiver):
	def __init__(self, receiverProxy):
		Receiver.__init__(self, 'bc780', receiverProxy)
	def invokeRadio(self, command, argz):
		"""
		invoke the external command line utility and return response
		"""
		commandLine = "%s %s%s" % (self.receiverProxy, command, argz)
		print commandLine

		temp1 = os.popen(commandLine).readlines()
		temp2 = temp1[0]

		try:
			ndx1 = temp2.rindex(command)
			ndx2 = temp2.index('\n', ndx1)
			return(temp2[ndx1:ndx2])
		except ValueError:
			return("NONE")

	def testRadio(self):
		"""
		return true if the scanner is awake and responsive
		"""
		result = self.invokeRadio("SI", "")
		print "::%s::" % result

		try:
			ndx1 = result.index("BC780XLT")
			return(True)
		except ValueError:
			return(False)

	def tuneRadio(self, frequency):
		"""
		tune scanner to specified frequency
		returns frequency as integer
		"""
		argz = "%8.8d?" % (frequency)

		exitFlag = False
		errorCounter = 0

		while ((exitFlag == False) and (errorCounter < 10)):
			result = self.invokeRadio("RF", argz)

			if result == 'NONE':
				print "--------------->receiver tune parse error noted"
				time.sleep(1)
				errorCounter += 1
			else:
				return(result[2:])

		print "--------------->receiver tune errors exceed retry limit"
		return(0)

	def getModulation(self):
		"""
		return current modulation mode
		"""
		exitFlag = False
		errorCounter = 0

		while ((exitFlag == False) and (errorCounter < 10)):
			result = self.invokeRadio("RM", "")

			if result == 'NONE':
				print "--------------->receiver modulation parse error noted"
				time.sleep(1)
				errorCounter += 1
			else:
				return(result[3:])

		print "--------------->receiver modulation errors exceed retry limit"
		return("NONE")

	def getRawSample(self):
		"""
		return current sample (signal strength and integer frequency)
		"""
		exitFlag = False
		errorCounter = 0

		command = "%s SG" % (self.receiverProxy)

		while ((exitFlag == False) and (errorCounter < 10)):
			temp1 = os.popen(command).readlines()
			temp2 = temp1[0]

			try:
				ndx1 = temp2.rindex('S')
				ndx2 = temp2.index(' ', ndx1)
				strength = temp2[ndx1+1:ndx2]

				ndx1 = temp2.rindex('F')
				ndx2 = temp2.index('\n', ndx1)
				frequency = temp2[ndx1+1:ndx2]

				return [int(strength), long(frequency)]
			except ValueError:
				print "--------------->receiver sample parse error noted"
				print command
				print temp2

				time.sleep(1)
				errorCounter += 1

		print "--------------->receiver sample errors exceed retry limit"
		return([0, 0])

	def sampleRadio(self, frequency):
		"""
		tune to frequency and sample signal strength
		return tuple of frequency, strength and modulation
		"""
		time.sleep(1)
		self.tuneRadio(frequency)

		time.sleep(1)
		modulation = self.getModulation()

		time.sleep(1)
		sample = self.getRawSample()

		return([sample[1], sample[0], modulation])

	def sampleBand(self, band):
		print 'sample band:%f %f' % (band.frequencyLow, band.frequencyHigh)

		lowFreq = int(band.frequencyLow * 10000)
		highFreq = int(band.frequencyHigh * 10000)
		stepFreq = int(band.frequencyStep * 10)

		print 'sample band:%d %d' % (lowFreq, highFreq)

		resultList = []
		currentFrequency = lowFreq
		while currentFrequency < highFreq:
			tempList = self.sampleRadio(currentFrequency)
			observation = Observation(currentFrequency, tempList[1], band.bandNdx)
			resultList.append(observation)
			currentFrequency += stepFreq
			
		return(resultList)

#
#
#
print 'start'

if __name__ == '__main__':
	rx = ReceiverBc780('/home/gsc/git/mellow-elephant-py/bin/sampler1a')
	if (rx.testRadio()):
		print 'radio test OK'
		print rx.tuneRadio(1241000)
		print rx.getModulation()
		print rx.getRawSample()
		print rx.sampleRadio(1241000)
	else:
		print 'radio test failure'

print 'stop'

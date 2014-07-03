#
# Title:Observation.py
# Description:observation container
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import time
import uuid

from datetime import datetime

class Observation:
	def __init__(self, frequency=0, sample=0, band=0):
		self.band = band
		self.frequency = frequency
		self.observationId = str(uuid.uuid4())
		self.sample = sample
		self.timeStampMs = int(1000 * time.time())

	def toDictionary(self):
		result = {}
		result['band'] = self.band
		result['frequency'] = self.frequency
		result['sample'] = self.sample
		result['timeStampMs'] = self.timeStampMs
		result['observationId'] = self.observationId
		return(result);

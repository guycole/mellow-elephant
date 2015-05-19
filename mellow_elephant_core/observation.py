#
# Title:observation.py
# Description:observation container
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import time
import uuid


class Observation:
    def __init__(self, sample=0, frequency=0, bandNdx=0):
        self.band = bandNdx
        self.frequency = frequency
        self.observationId = str(uuid.uuid4())
        self.sample = sample
        self.timeStampMs = int(1000 * time.time())

    def __str__(self):
        buffer = "%d:%d:%d:%d" % (self.band, self.sample, self.frequency, self.timeStampMs)
        return buffer

    def toDictionary(self):
        result = {}
        result['band'] = self.band
        result['frequency'] = self.frequency
        result['sample'] = self.sample
        result['timeStampMs'] = self.timeStampMs
        result['observationId'] = self.observationId
        return(result)

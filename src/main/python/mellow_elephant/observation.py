#
# Title:observation.py
# Description:observation container
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import time

class Observation:
    def __init__(self, sample=0, frequency=0):
        self.frequency = frequency
        self.sample = sample
        self.sample_time = int(time.time())

    def __str__(self):
        buffer = "%d:%d:%d" % (self.sample, self.frequency, self.sample_time)
        return buffer

    def to_dictionary(self):
        result = {}
        result['frequency'] = self.frequency
        result['sample'] = self.sample
        result['time'] = self.sample_time
        return result
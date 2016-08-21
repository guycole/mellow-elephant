#! /usr/bin/python
#
# Title:collection.py
# Description: mellow elephant collection
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import pickle
import sys
import yaml

from band_bc780 import BandBc780Factory
from pickled_band import PickledBand
from pid_lock import PidLock
from receiver import ReceiverFactory

class MellowElephant:

    def band_work(self, band_ndx, receiver):
        band_factory = BandBc780Factory()
        frequency_band = band_factory.factory(band_ndx)
        observations = receiver.sample_band(frequency_band)

        pickled_band = PickledBand(installation, band_ndx, observations)
        pickle.dump(pickled_band, open(pickled_band.get_filename(data_directory), "wb"))

    def runner(self, receiver):
        if run_direction == 'low2high':
            for band in frequency_bands:
                self.band_work(band, receiver)
        else:
            for band in reversed(frequency_bands):
                self.band_work(band, receiver)
	
    def execute(self):
        pid_lock = PidLock()
        if pid_lock.lock_test(pid_lock_file):
            print 'pid lock noted'
        else:
            print 'pid lock fail'
            pid_lock.write_lock(pid_lock_file)

            receiver_factory = ReceiverFactory()
            current_receiver = receiver_factory.factory(receiver_type, serial_device)

	    if run_mode == 'always':
                while True:
                    self.runner(current_receiver)    
            else:
                self.runner(current_receiver)    

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

    data_directory = configuration['dataDirectory']

    frequency_bands = configuration['frequencyBands']

    installation = configuration['installationId']

    receiver_type = configuration['receiverType']

    serial_device = configuration['serialDevice']

    pid_lock_file = configuration['pidLockFile']

    run_direction = configuration['runDirection']
    run_mode = configuration['runMode']

    driver = MellowElephant()
    driver.execute()

print 'stop'

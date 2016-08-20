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
from pid_lock import PidLock
from receiver import ReceiverFactory

class MellowElephant:

    def upload(self, band_ndx, receiver, observations):
        print 'yyy'
#        for observation in observations:
#            print observation

        #pickle.dump(observations, open(currentSortie.getPickledObservationName(self.dataDirectory, band.bandNdx), "wb"))

        # write sortie to signal completion
        #pickle.dump(currentSortie, open(currentSortie.getPickledSortieName(self.dataDirectory), "wb"))

    def band_work(self, band_ndx, receiver):
        band_factory = BandBc780Factory()
        frequency_band = band_factory.factory(band_ndx)
        observations = receiver.sample_band(frequency_band)
        self.upload(band_ndx, receiver, observations)
        print frequency_band

    def execute(self):
        pid_lock = PidLock()
        if pid_lock.lock_test(pid_lock_file):
            print 'pid lock noted'
        else:
            print 'pid lock fail'
            pid_lock.write_lock(pid_lock_file)

            receiver_factory = ReceiverFactory()
            current_receiver = receiver_factory.factory(receiver_type, receiver_proxy)

            if run_direction == 'low2high':
                for band in frequency_bands:
                    self.band_work(band, current_receiver)
            else:
                for band in reversed(frequency_bands):
                    self.band_work(band, current_receiver)

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

    frequency_bands = configuration['frequencyBands']

    receiver_type = configuration['receiverType']
    receiver_proxy = configuration['receiverProxy']

    pid_lock_file = configuration['pidLockFile']

    run_direction = configuration['runDirection']
    run_mode = configuration['runMode']

    s3bucket = configuration['s3bucket']

    driver = MellowElephant()
    driver.execute()

print 'stop'

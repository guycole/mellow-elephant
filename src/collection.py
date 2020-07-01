#
# Title:collection.py
# Description: mellow elephant collection
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import pickle
import sys
import yaml

from band_bc780 import BandBc780Factory
from pickled_band import PickledBand
from pid_lock import PidLock
from receiver import ReceiverFactory

class Collection:

    def band_work(self, band_ndx, receiver):
        band_factory = BandBc780Factory()
#        frequency_band = band_factory.factory(band_ndx)
#        observations = receiver.sample_band(frequency_band)

#        pickled_band = PickledBand(installation, band_ndx, observations)
#        pickle.dump(pickled_band, open(pickled_band.get_filename(pickle_directory), "wb"))

    def runner(self, frequency_bands:list, receiver:object, run_direction:str):
        if run_direction == 'low2high':
            for band in frequency_bands:
                self.band_work(band, receiver)
        else:
            for band in reversed(frequency_bands):
                self.band_work(band, receiver)

    def execute(self, configuration:dict):
#        pickle_directory = configuration['pickleDirectory']
        frequency_bands = configuration['frequencyBands']
        installation = configuration['installationId']
        receiver_type = configuration['receiverType']
        serial_device = configuration['serialDevice']
        pid_lock_file = configuration['pidLockFile']
        run_direction = configuration['runDirection']
        run_mode = configuration['runMode']

        pid_lock = PidLock()
        if pid_lock.lock_test(pid_lock_file):
            print('active pid lock noted')
        else:
            print('write fresh pid lock')
            pid_lock.write_lock(pid_lock_file)

            receiver_factory = ReceiverFactory()
            current_receiver = receiver_factory.factory(receiver_type, serial_device)

            if run_mode == 'always':
                while True:
                    self.runner(frequency_bands, current_receiver, run_direction)
            else:
                self.runner(frequency_bands, current_receiver, run_direction)

print('start')

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "config.yaml"

    with open(file_name, "r") as infile:
        try:
            collection = Collection()
            collection.execute(yaml.load(infile, Loader=yaml.FullLoader))
        except yaml.YAMLError as exception:
            print(exception)

print('stop')

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
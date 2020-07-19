#
# Title:collection.py
# Description: mellow elephant collection
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import logging
import pickle
import sys
import yaml

from pickled_band import PickledBand
from pid_lock import PidLock
from receiver import ReceiverFactory

class Collection:
    def __init__(self, logger_level:int):
        logging.basicConfig(format='%(asctime)s %(message)s', level=logger_level)

        self.logger = logging.getLogger()
        self.logger.debug('debug level message')
        self.logger.info('info level message')
        self.logger.warning('warning level message')
        self.logger.error('error level message')
        self.logger.critical('critical level message')

    def band_work(self, band_ndx:int, receiver:object) -> list:
        """
        Sample a frequency band
        :param band_ndx: index into receiver specific band table
        :param receiver: object
        :return: observations list
        """
        self.logger.info(f"now walking band {band_ndx} {receiver}")

        return receiver.sample_band(band_ndx)

    def runner(self, frequency_bands:list, receiver:object, installation:str, pickle_directory:str):
        """
        Drive a collection pass (sample all specified frequency bands)
        :param frequency_bands: list of indices into receiver specific catalog
        :param receiver: object
        :param installation: unique installation identifier
        :param pickle_directory: directory to contain serialized observations
        :return:
        """
        for band_ndx in frequency_bands:
            observations = self.band_work(band_ndx, receiver)

            pickled_band = PickledBand(installation, band_ndx, observations)
            pickle.dump(pickled_band, open(pickled_band.get_filename(pickle_directory), "wb"))

    def execute(self, configuration:dict):
        pickle_directory = configuration['pickleDirectory']
        frequency_bands = configuration['frequencyBands']
        installation = configuration['installationId']
        receiver_type = configuration['receiverType']
        serial_device = configuration['serialDevice']
        pid_lock_file = configuration['pidLockFile']
        run_mode = configuration['runMode']

        pid_lock = PidLock()
        if pid_lock.lock_test(pid_lock_file):
            self.logger.info('active pid lock noted')
        else:
            self.logger.info('write fresh pid lock')
            pid_lock.write_lock(pid_lock_file)

            receiver_factory = ReceiverFactory()
            current_receiver = receiver_factory.factory(receiver_type, serial_device)

            run_flag = True
            while run_flag:
                self.runner(frequency_bands, current_receiver, installation, pickle_directory)
                if run_mode == 'once':
                    run_flag = False

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
#            collection = Collection(logging.INFO)
            collection = Collection(logging.DEBUG)
            collection.execute(yaml.load(infile, Loader=yaml.FullLoader))
        except yaml.YAMLError as exception:
            print(exception)

print('stop')

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
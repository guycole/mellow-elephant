#
# Title:collection.py
# Description: mellow elephant collection
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import logging
import sys
import yaml

from pickled_band import PickledBand
from pid_lock import PidLock
from receiver import ReceiverFactory


class Collection:
    def __init__(self, logger_level: int, configuration: dict):
        logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)

        self.logger = logging.getLogger()
#        self.logger.debug("debug level message")
#        self.logger.info("info level message")
#        self.logger.warning("warning level message")
#        self.logger.error("error level message")
#        self.logger.critical("critical level message")

        self.pickle_directory = configuration["pickleDirectory"]
        self.frequency_bands = configuration["frequencyBands"]
        self.installation = configuration["installationId"]
        self.receiver_type = configuration["receiverType"]
        self.serial_device = configuration["serialDevice"]
        self.pid_lock_file = configuration["pidLockFile"]
        self.run_mode = configuration["runMode"]

    def sample_band(self, band_ndx: int, receiver: object) -> list:
        """
        Sample a frequency band
        :param band_ndx: index into receiver specific band table
        :param receiver: object
        :return: observations list
        """
        log_message = "now walking band %d %s" % (band_ndx, receiver)
        self.logger.info(log_message)

        return receiver.sample_band(band_ndx)

    def runner(self, receiver: object):
        """
        Drive a collection pass (sample all specified frequency bands)
        :param receiver: object
        :return:
        """
        fresh_directory = "%s/fresh" % self.pickle_directory

        for band_ndx in self.frequency_bands:
            observations = self.sample_band(band_ndx, receiver)
            pickled_band = PickledBand(self.installation, band_ndx, observations)

            with open(pickled_band.get_filename(fresh_directory), "w") as writer:
                writer.write(pickled_band.to_json)

    def execute(self):
        pid_lock = PidLock()
        if pid_lock.lock_test(self.pid_lock_file):
            self.logger.info("active pid lock noted")
        else:
            self.logger.info("write fresh pid lock")
            pid_lock.write_lock(self.pid_lock_file)

            receiver_factory = ReceiverFactory()
            current_receiver = receiver_factory.factory(
                self.receiver_type, self.serial_device
            )

            if current_receiver.test_radio() is True:
                self.logger.info("receiver noted")
            else:
                self.logger.error("unable to connect to radio")
                return

            run_flag = True
            while run_flag:
                self.runner(current_receiver)
                if self.run_mode == "once":
                    run_flag = False


print("start")

#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "config.yaml"

    logging_level = logging.INFO
    logging_level = logging.DEBUG

    with open(file_name, "r") as infile:
        try:
            collection = Collection(
                logging_level, yaml.load(infile, Loader=yaml.FullLoader)
            )
            collection.execute()
        except yaml.YAMLError as exception:
            print(exception)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

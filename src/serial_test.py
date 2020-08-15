#
# Title:serial_test.py
# Description: test serial
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import logging
import sys
import yaml

from receiver import ReceiverFactory

class SerialTest:
    def __init__(self, logger_level: int, configuration: dict):
        logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)

        self.logger = logging.getLogger()
        self.logger.debug("debug level message")
        self.logger.info("info level message")
        self.logger.warning("warning level message")
        self.logger.error("error level message")
        self.logger.critical("critical level message")

        self.receiver_type = configuration["receiverType"]
        self.serial_device = configuration["serialDevice"]

        receiver_factory = ReceiverFactory()
        current_receiver = receiver_factory.factory(self.receiver_type, self.serial_device)

        if current_receiver.test_radio() is True:
            self.logger.info("receiver noted")
        else:
            self.logger.error("unable to connect to radio")


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
            serial_test = SerialTest(
                logging_level, yaml.load(infile, Loader=yaml.FullLoader)
            )
            serial_test.execute()
        except yaml.YAMLError as exception:
            print(exception)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

#
# Title:processing.py
# Description: mellow elephant processing
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import json
import logging
import os
import sys
import yaml


class Processing:
    def __init__(self, logger_level: int):
        logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)

        self.logger = logging.getLogger()
        self.logger.debug("debug level message")
        self.logger.info("info level message")
        self.logger.warning("warning level message")
        self.logger.error("error level message")
        self.logger.critical("critical level message")

    def moving_average(self, observations):
        ma_average = 0
        ma_buffer = []
        ma_length = 5
        ma_sum = 0

        results = []
        # expect observations to be sorted by frequency, low to high
        for observation in observations:
            if len(ma_buffer) > ma_length:
                ma_buffer.pop(0)

            ma_buffer.append(observation['strength'])
            ma_sum = sum(ma_buffer)
            observation['moving_average'] = int(ma_sum/len(ma_buffer))
            results.append(observation)

        return results

    def write_observations(self, db_directory, installation, sortie, observations):
        directory_name = f"{db_directory}/{installation}"
        if os.path.exists(directory_name) is False:
            os.mkdir(directory_name, 0o775)

        for observation in observations:
            print(observation.keys())
            file_name = f"{directory_name}/{observation['frequency']}"
            with open(f"{file_name}", "a+") as writer:
                writer.write(f"{observation['strength']}|{observation['modulation']}|{observation['timestamp']}|{observation['moving_average']}|{sortie}\n")

    def write_sortie(self, db_directory, installation, sortie, create_time, band_ndx):
        with open(f"{db_directory}/sortie.log", "a+") as writer:
            writer.write(f"{band_ndx}|{create_time}|{installation}|{sortie}\n")

    def process_candidate(self, file_name, db_directory):
        with open(file_name, newline='') as fp:
            raw_buffer = fp.readlines()
            if len(raw_buffer) == 1:
                dict_buffer = json.loads(raw_buffer[0])
                if dict_buffer['version'] == 1:
                    self.write_sortie(db_directory, dict_buffer['installation'], dict_buffer['sortie'], dict_buffer['create_time'], dict_buffer['band_ndx'])
                    cooked = self.moving_average(dict_buffer['observations'])
                    self.write_observations(db_directory, dict_buffer['installation'], dict_buffer['sortie'], cooked)

                    # write peakers
                    # write graph

    def execute(self, configuration: dict):
        db_directory = configuration["dbDirectory"]

        pickle_directory = configuration["pickleDirectory"]
        fresh_directory = f"{pickle_directory}/fresh"
        process_directory = f"{pickle_directory}/processing"

        candidates = os.listdir(path=fresh_directory)
        for candidate in candidates:
            self.logger.info(f"process {candidate}")
            self.process_candidate(f"{fresh_directory}/{candidate}", db_directory)

            command = f"mv {fresh_directory}/{candidate} {process_directory}"
            print(command)

print("start")

#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "config.yaml"

    with open(file_name, "r") as infile:
        try:
            #            collection = Collection(logging.INFO)
            processing = Processing(logging.DEBUG)
            processing.execute(yaml.load(infile, Loader=yaml.FullLoader))
        except yaml.YAMLError as exception:
            print(exception)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

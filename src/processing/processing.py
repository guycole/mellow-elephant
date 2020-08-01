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

from database import DataBase


class Processing:
    def __init__(self, logger_level: int):
        logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)

        self.logger = logging.getLogger()
        self.logger.debug("debug level message")
        self.logger.info("info level message")
        self.logger.warning("warning level message")
        self.logger.error("error level message")
        self.logger.critical("critical level message")

    def observation_db(self, db_directory, observations, band_ndx, sortie_key, db):
        observation_file = f"{db_directory}/observation.sqlite"

        if os.path.exists(observation_file) and os.path.isfile(observation_file):
            pass
        else:
            db.create_observation(observation_file)

        db.write_observation(observation_file, observations, band_ndx, sortie_key)

    def sortie_db(self, db_directory, band_ndx, create_time, installation_id, sortie_key, db):
        sortie_file = f"{db_directory}/sortie.sqlite"

        if os.path.exists(sortie_file) and os.path.isfile(sortie_file):
            selected = db.select_sortie(sortie_file, sortie_key)
            if len(selected) < 1:
                db.write_sortie(sortie_file, band_ndx, create_time, installation_id, sortie_key)
            else:
                self.logger.info(f"skipping duplicate sortie:{sortie_key}")
        else:
            db.create_sortie(sortie_file)
            db.write_sortie(sortie_file, band_ndx, create_time, installation_id, sortie_key)

    def fresh_candidate(self, file_name, db_directory, db):
        self.logger.info(f"fresh:{file_name}")

        with open(file_name, newline='') as fp:
            raw_buffer = fp.readlines()
            if len(raw_buffer) == 1:
                dict_buffer = json.loads(raw_buffer[0])

                band_ndx = dict_buffer['band_ndx']
                create_time = dict_buffer['create_time']
                installation_id = dict_buffer['installation']
                observations = dict_buffer['observations']
                sortie_key = dict_buffer['sortie']
                version = dict_buffer['version']

                if version == 1:
                    self.sortie_db(db_directory, band_ndx, create_time, installation_id, sortie_key, db)
                    self.observation_db(db_directory, observations, band_ndx, sortie_key, db)
                else:
                    self.logger.error("unsupported json version")
                    return -1

                    # write peakers
                    # write graph

    def execute(self, configuration, database):
        db_directory = configuration["dbDirectory"]

        pickle_directory = configuration["pickleDirectory"]
        archive_directory = f"{pickle_directory}/archive"
        fresh_directory = f"{pickle_directory}/fresh"

        candidates = os.listdir(path=fresh_directory)
        self.logger.info(f"process population:{len(candidates)}")
        for candidate in candidates:
            raw_filename = f"{fresh_directory}/{candidate}"
            self.fresh_candidate(raw_filename, db_directory, database)

            command = f"mv {raw_filename} {archive_directory}"
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

    logging_level = logging.INFO
    logging_level = logging.DEBUG

    database = DataBase(logging_level)

    with open(file_name, "r") as infile:
        try:
            processing = Processing(logging_level)
            processing.execute(yaml.load(infile, Loader=yaml.FullLoader), database)
        except yaml.YAMLError as exception:
            print(exception)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

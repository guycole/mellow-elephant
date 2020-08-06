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

from band_bc780 import BandBc780Factory

from database import DataBase


class Processing:
    def __init__(self, logger_level: int, configuration: dict):
        logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)

        self.logger = logging.getLogger()
        self.logger.debug("debug level message")
        self.logger.info("info level message")
        self.logger.warning("warning level message")
        self.logger.error("error level message")
        self.logger.critical("critical level message")

        self.pickle_directory = configuration["pickleDirectory"]
        self.archive_directory = "%s/archive" % self.pickle_directory
        self.fresh_directory = "%s/fresh" % self.pickle_directory

        self.db_directory = configuration["dbDirectory"]
        self.graph_directory = configuration["grafDirectory"]

    def graph_write(self, file_name, observations, band_ndx, sortie_key):
        graph_file_name = "%s/%s" % (self.graph_directory, file_name.replace('json', 'png'))
        plot_file_name = "/tmp/plot.dem"
        strength_file_name = "/tmp/strength.dat"

        bc780band_factory = BandBc780Factory()
        bc780band = bc780band_factory.factory(band_ndx)

        plot_title = "set title '%f mHz to %f mHz in %f kHz steps (band %d)'\n" % (bc780band.frequency_low, bc780band.frequency_high, bc780band.frequency_step, bc780band.band_ndx)

        with open(strength_file_name, "w") as writer:
            for observation in observations:
                frequency = observation['frequency']
                moving_average = observation['moving_average']
                strength = observation['strength']

                writer.write("%f %d %d\n" % (frequency/10000.0, strength, moving_average))

        with open(plot_file_name, "w") as writer:
            writer.write("set terminal png small\n")
            writer.write("set timestamp\n")
            writer.write("set grid\n")
            writer.write("set style data line\n")
            writer.write("set output '%s'\n" % graph_file_name)
            writer.write(plot_title)
            writer.write("plot '%s' using 1:2 with lp, '' using 1:3 with lines\n" % strength_file_name)

        command = "%s %s" % ('/usr/local/bin/gnuplot', plot_file_name)
        os.system(command)

        os.unlink(plot_file_name)
        os.unlink(strength_file_name)

    def observation_db(self, observations, band_ndx, sortie_key, db):
        observation_file = "%s/observation.sqlite" % self.db_directory

        if os.path.exists(observation_file) and os.path.isfile(observation_file):
            pass
        else:
            db.create_observation(observation_file)

        db.write_observation(observation_file, observations, band_ndx, sortie_key)

    def peaker_db(self, observations, band_ndx, sortie_key, db):
        peakers_file = "%s/peakers.sqlite" % self.db_directory

        if os.path.exists(peakers_file) and os.path.isfile(peakers_file):
            pass
        else:
            db.create_peaker(peakers_file)

        db.write_peaker(peakers_file, observations)

    def sortie_db(self, band_ndx, create_time, installation_id, sortie_key, db):
        sortie_file = "%s/sortie.sqlite" % self.db_directory

        if os.path.exists(sortie_file) and os.path.isfile(sortie_file):
            selected = db.select_sortie(sortie_file, sortie_key)
            if len(selected) < 1:
                db.write_sortie(sortie_file, band_ndx, create_time, installation_id, sortie_key)
            else:
                self.logger.info("skipping duplicate sortie: %s" % sortie_key)
        else:
            db.create_sortie(sortie_file)
            db.write_sortie(sortie_file, band_ndx, create_time, installation_id, sortie_key)

    def fresh_candidate(self, file_name, db):
        self.logger.info("fresh:%s" % file_name)

        full_file_name = "%s/%s" % (self.fresh_directory, file_name)
        with open(full_file_name, newline='') as fp:
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
                    self.sortie_db(band_ndx, create_time, installation_id, sortie_key, db)
                    self.observation_db(observations, band_ndx, sortie_key, db)
                    self.peaker_db(observations, band_ndx, sortie_key, db)
                    self.graph_write(file_name, observations, band_ndx, sortie_key)
                else:
                    self.logger.error("unsupported message version")
                    return -1

    def execute(self, db):
        candidates = os.listdir(path=self.fresh_directory)
        for candidate in candidates:
            self.fresh_candidate(candidate, db)

#            command = "mv %s %s" % (raw_filename, self.archive_directory)
#            print(command)

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
            processing = Processing(logging_level, yaml.load(infile, Loader=yaml.FullLoader))
            processing.execute(database)
        except yaml.YAMLError as exception:
            print(exception)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

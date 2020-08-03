#
# Title:database.py
# Description: mellow elephant database
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import logging
import sqlite3

class DataBase:
    def __init__(self, logger_level: int):
        logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)
        self.logger = logging.getLogger()

    def create_observation(self, observation_file):
        self.logger.info("create observation db table")

        create_table = "CREATE TABLE observation(sortie_key text, band_ndx integer, strength integer, frequency integer, modulation text, time_stamp integer, moving_average integer, peaker integer)"

        create_index1 = "CREATE INDEX ndx1 ON observation(sortie_key)"
        create_index2 = "CREATE INDEX ndx2 ON observation(band_ndx)"
        create_index3 = "CREATE INDEX ndx3 ON observation(frequency)"

        connection = sqlite3.connect(observation_file)
        connection.execute(create_table)
        connection.execute(create_index1)
        connection.execute(create_index2)
        connection.execute(create_index3)
        connection.commit()
        connection.close()

    def write_observation(self, observation_file, observations, band_ndx, sortie_key):
        # self.logger.info("write observation db table")

        connection = sqlite3.connect(observation_file)

        for observation in observations:
            strength = observation['strength']
            frequency = observation['frequency']
            modulation = observation['modulation']
            time_stamp = observation['time_stamp']
            moving_average = observation['moving_average']
            peaker = observation['peaker']

            insert = "INSERT INTO observation(sortie_key, band_ndx, strength, frequency, modulation, time_stamp, moving_average, peaker) VALUES('%s', %d, %d, %d, '%s', %d, %d, %d)" % (sortie_key, band_ndx, strength, frequency, modulation, time_stamp, moving_average, peaker)
            connection.execute(insert)

        connection.commit()
        connection.close()

    def create_peaker(self, peaker_file):
        self.logger.info("create peaker db table")

        create_table = "CREATE TABLE peaker(frequency integer PRIMARY KEY, present integer, not_present integer)"

        connection = sqlite3.connect(peaker_file)
        connection.execute(create_table)
        connection.commit()
        connection.close()

    def select_peaker(self, peaker_file, frequency):
        # self.logger.info("select peaker db")

        select = "SELECT frequency, present, not_present FROM peaker WHERE frequency = %d" % frequency

        connection = sqlite3.connect(peaker_file)
        cursor = connection.cursor()
        cursor.execute(select)
        return cursor.fetchall()

    def write_peaker(self, peaker_file, observations):
        connection = sqlite3.connect(peaker_file)

        for observation in observations:
            frequency = observation['frequency']
            peaker = observation['peaker']

            selected = self.select_peaker(peaker_file, frequency)

            if len(selected) > 0:
                valuez = selected[0]
                present = valuez[1]
                not_present = valuez[2]

                if peaker > 0:
                    present = present+1
                    update = "UPDATE peaker SET present=%d WHERE frequency=%d" % (present, frequency)
                else:
                    not_present = not_present+1
                    update = "UPDATE peaker SET not_present=%d WHERE frequency=%d" % (not_present, frequency)

                connection.execute(update)
            else:
                if peaker > 0:
                    insert = "INSERT INTO peaker(frequency, present, not_present) VALUES(%d, 1, 0)" % frequency
                else:
                    insert = "INSERT INTO peaker(frequency, present, not_present) VALUES(%d, 0, 1)" % frequency

                connection.execute(insert)

        connection.commit()
        connection.close()

    def create_sortie(self, sortie_file):
        self.logger.info("create sortie db table")

        create_table = "CREATE TABLE sortie(sortie_key text PRIMARY KEY, band_ndx integer, create_time integer, installation_id text)"

        connection = sqlite3.connect(sortie_file)
        connection.execute(create_table)
        connection.commit()
        connection.close()

    def select_sortie(self, sortie_file, sortie_key):
        # self.logger.info("select sortie db")

        select = "SELECT sortie_key, band_ndx, create_time, installation_id FROM sortie WHERE sortie_key = '%s'" % sortie_key

        connection = sqlite3.connect(sortie_file)
        cursor = connection.cursor()
        cursor.execute(select)
        return cursor.fetchall()

    def write_sortie(self, sortie_file,  band_ndx, create_time, installation_id, sortie_key):
        # self.logger.info("write sortie db table")

        insert = "INSERT INTO sortie(sortie_key, band_ndx, create_time, installation_id) VALUES('%s', %d, %d, '%s')" % (sortie_key, band_ndx, create_time, installation_id)

        connection = sqlite3.connect(sortie_file)
        connection.execute(insert)
        connection.commit()
        connection.close()
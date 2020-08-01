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
        self.logger.info(f"create observation db table")

        create_table = f"CREATE TABLE observation(sortie_key text, band_ndx integer, strength integer, frequency integer, modulation text, time_stamp integer, moving_average integer, peaker integer)"

        create_index1 = f"CREATE INDEX ndx1 ON observation(sortie_key)"
        create_index2 = f"CREATE INDEX ndx2 ON observation(band_ndx)"
        create_index3 = f"CREATE INDEX ndx3 ON observation(frequency)"

        connection = sqlite3.connect(observation_file)
        connection.execute(create_table)
        connection.execute(create_index1)
        connection.execute(create_index2)
        connection.execute(create_index3)
        connection.commit()
        connection.close()

    def write_observation(self, observation_file, observations, band_ndx, sortie_key):
        connection = sqlite3.connect(observation_file)

        for observation in observations:
            print(observation)
            strength = observation['strength']
            frequency = observation['frequency']
            modulation = observation['modulation']
            time_stamp = observation['time_stamp']
            moving_average = observation['moving_average']
            peaker = observation['peaker']

            insert = f"INSERT INTO observation(sortie_key, band_ndx, strength, frequency, modulation, time_stamp, moving_average, peaker) VALUES('{sortie_key}', {band_ndx}, {strength}, {frequency}, '{modulation}', {time_stamp}, {moving_average}, {peaker})"
            connection.execute(insert)

        connection.commit()
        connection.close()

    def create_peaker(self, peaker_file):
        self.logger.info(f"create peaker db table")

        create_table = f"CREATE TABLE peaker(sortie_key text, band_ndx integer, strength integer, frequency integer, modulation text, time_stamp integer, moving_average integer, peaker integer)"

        create_index1 = f"CREATE INDEX ndx1 ON peaker(sortie_key)"
        create_index2 = f"CREATE INDEX ndx2 ON peaker(band_ndx)"
        create_index3 = f"CREATE INDEX ndx3 ON peaker(frequency)"

        connection = sqlite3.connect(peaker_file)
        connection.execute(create_table)
        connection.execute(create_index1)
        connection.execute(create_index2)
        connection.execute(create_index3)
        connection.commit()
        connection.close()

    def write_peaker(self, peaker_file, observations, band_ndx, sortie_key):
        connection = sqlite3.connect(peaker_file)

        for observation in observations:
            print(observation)
            strength = observation['strength']
            frequency = observation['frequency']
            modulation = observation['modulation']
            time_stamp = observation['time_stamp']
            moving_average = observation['moving_average']
            peaker = observation['peaker']

            if peaker > 0:
                insert = f"INSERT INTO peaker(sortie_key, band_ndx, strength, frequency, modulation, time_stamp, moving_average, peaker) VALUES('{sortie_key}', {band_ndx}, {strength}, {frequency}, '{modulation}', {time_stamp}, {moving_average}, {peaker})"
                connection.execute(insert)

        connection.commit()
        connection.close()

    def create_sortie(self, sortie_file):
        self.logger.info(f"create sortie db table")

        create_table = f"CREATE TABLE sortie(sortie_key text PRIMARY KEY, band_ndx integer, create_time integer, installation_id text)"

        connection = sqlite3.connect(sortie_file)
        connection.execute(create_table)
        connection.commit()
        connection.close()

    def select_sortie(self, sortie_file, sortie_key):
        self.logger.info(f"select sortie db")

        select = f"SELECT sortie_key, band_ndx, create_time, installation_id FROM sortie WHERE sortie_key = '{sortie_key}'"

        connection = sqlite3.connect(sortie_file)
        cursor = connection.cursor()
        cursor.execute(select)
        return cursor.fetchall()

    def write_sortie(self, sortie_file,  band_ndx, create_time, installation_id, sortie_key):
        self.logger.info(f"write sortie db table")

        insert = f"INSERT INTO sortie(sortie_key, band_ndx, create_time, installation_id) VALUES('{sortie_key}', {band_ndx}, {create_time}, '{installation_id}')"

        connection = sqlite3.connect(sortie_file)
        connection.execute(insert)
        connection.commit()
        connection.close()
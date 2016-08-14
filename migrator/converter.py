#!/usr/bin/python
#
# Title:converter.py
# Description: pickle each sortie within mysql
# Development Environment:OS X 10.8.5/Python 2.7.2
# Author:G.S. Cole (guycole at gmail dot com)
#
import pickle
import sys
import uuid
import yaml

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pickled_band import PickledBand

from sql_table import Observation
from sql_table import Sortie

print 'start converter'

class MellowElephantConverter:

    def write_observations(self, session, sortie_uuid):
        print sortie_uuid

        band = PickledBand('name', 'note', sortie_uuid, 'install')

        selected_set = session.query(Observation).filter_by(sortie_uuid = sortie_uuid).order_by(Observation.time_stamp).all()
        for select in selected_set:
            print "%d %s %s" % (select.frequency, select.sortie_uuid, select.time_stamp)
            band.add_observation(select.frequency, select.sample, select.time_stamp)

        pickle.dump(band, open('/tmp/xxx', "wb"))

    def add_observation(self, frequency, sample, time_stamp):
        observation = (frequency, sample, time_stamp)
        observations.append(observation)

    def execute(self, task_id):
        print "execute:%s" % task_id

        mysql_url = "mysql://%s:%s@%s:3306/%s" % (mysql_username, mysql_password, mysql_hostname, mysql_database)
        engine = create_engine(mysql_url, echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()

        sorties = session.query(Sortie).all()
        for sortie in sorties:
            self.write_observations(session, sortie.sortie_uuid)
            break;
#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        fileName = 'config.yaml'

    configuration = yaml.load(file(fileName))

    rm_command = configuration['rmCommand']

    export_dir = configuration['exportDir']

    mysql_username = configuration['mySqlUserName']
    mysql_password = configuration['mySqlPassWord']
    mysql_hostname = configuration['mySqlHostName']
    mysql_database = configuration['mySqlDataBase']

    driver = MellowElephantConverter()
    driver.execute(uuid.uuid4())

print 'stop converter'

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***

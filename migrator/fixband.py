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

from band_bc780 import BandBc780
from band_bc780 import BandBc780Factory

from sql_table import Installation
from sql_table import Observation
from sql_table import Sortie

print 'start converter'

class MellowElephantFixBand:

    def execute(self, task_id):
        print "execute:%s" % task_id

        mysql_url = "mysql://%s:%s@%s:3306/%s" % (mysql_username, mysql_password, mysql_hostname, mysql_database)
        engine = create_engine(mysql_url, echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()

        factory = BandBc780Factory()

        candidates = session.query(Observation).filter_by(band = "test").all()
        for candidate in candidates:
            ndx = factory.matcher(candidate.frequency)
            print "%d %s" % (ndx.band_ndx, ndx.band_name)
#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        fileName = 'config.yaml'

    configuration = yaml.load(file(fileName))

    mysql_username = configuration['mySqlUserName']
    mysql_password = configuration['mySqlPassWord']
    mysql_hostname = configuration['mySqlHostName']
    mysql_database = configuration['mySqlDataBase']

    driver = MellowElephantFixBand()
    driver.execute(uuid.uuid4())

print 'stop converter'

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***

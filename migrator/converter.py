#!/usr/bin/python
#
# Title:converter.py
# Description: pickle each sortie within mysql
# Development Environment:OS X 10.8.5/Python 2.7.2
# Author:G.S. Cole (guycole at gmail dot com)
#
import uuid

print 'start converter'

class MellowElephantConverter:

    def execute(self, task_id):
        print "execute:%s" % task_id

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

    export_path = configuration['exportPath']
    root_path = configuration['rootPath']

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
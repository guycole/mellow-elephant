#! /usr/bin/python
#
# Title:Converter.py
# Description:convert existing mellow elephant datum
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import pgdb
import pickle
import sys
import yaml

class Converter:
	def execute(self, dataDirectory):
		self.dataDirectory = dataDirectory

		db = pgdb.connect(database = 'mellow_elephant1b', user = 'gsc', password = '')

		passNdx = 0
		while passNdx < 400:
			sql = "select id, sample, threshold, frequency, band_key from raw_sample_a where pass = %d order by frequency" % (passNdx)
			cursor = db.cursor()
			cursor.execute(sql)
			rowz = cursor.fetchall()
			cursor.close()

			print "pass:%d %d" % (passNdx, len(rowz))

			passNdx += 1

print 'start'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
	if len(sys.argv) > 1:
		fileName = sys.argv[1]
	else:
		fileName = "config.yaml"

	configuration = yaml.load(file(fileName))

	dataDirectory = configuration['dataDirectory']
	print dataDirectory

	converter = Converter()
	converter.execute(dataDirectory)

print 'stop'

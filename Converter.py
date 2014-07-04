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

import time
import datetime
#from datetime import date

from BandBc780 import BandBc780Factory

from Observation import Observation
from Sortie import Sortie


class Converter:

#[18427L, 82, 4045750L, '18a', '2013-02-08 02:57:38.465818-08']
#2013-05-08 13:08:33-07

	def convertTime(self, arg):
		print arg
		ndx = arg.rfind('-')
		offset = arg[ndx+1:]

		ndx = arg.rfind('.')
		if ndx < 0:
			ndx = arg.rfind('-')

		temp = arg[:ndx]
		localSeconds = time.mktime(time.strptime(temp, "%Y-%m-%d %H:%M:%S"))
		gmtSeconds = localSeconds + int(offset) * 60 * 60

		return int(gmtSeconds * 1000)

	def processPass(self, rowz):
		sortie = Sortie(self.installationId, "converted sortie")
                print "createSortie:%s" % sortie.sortieId

		os.mkdir(sortie.getDirectory(self.dataDirectory))

		bandFactory = BandBc780Factory()

		firstFlag = 0
		resultList = []
		for row in rowz:
			frequency = row[2]
			sample = row[1]
			band = bandFactory.matcher(row[2])
			timeStampMs = self.convertTime(row[4])
			observation = Observation(frequency, sample, band)
			observation.timeStampMs = timeStampMs
			resultList.append(observation)

			if firstFlag == 0:
				firstFlag = 1
				sortie.timeStampMs = timeStampMs

		pickle.dump(resultList, open(sortie.getPickledObservationName(self.dataDirectory, 0), "wb"))
		pickle.dump(sortie, open(sortie.getPickledSortieName(self.dataDirectory), "wb"))

	def execute(self, installationId, dataDirectory):
		self.dataDirectory = dataDirectory
		self.installationId = installationId

		db = pgdb.connect(database = 'mellow_elephant1b', user = 'gsc', password = '')

		passNdx = 62
		while passNdx < 400:
			sql = "select id, sample, frequency, band_key, time_stamp from raw_sample_a where pass = %d order by frequency" % (passNdx)
			cursor = db.cursor()
			cursor.execute(sql)
			rowz = cursor.fetchall()
			cursor.close()
			
			print "pass:%d %d" % (passNdx, len(rowz))

			if len(rowz) > 39000:
				self.processPass(rowz)

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

	installationId = configuration['installationId']
        print installationId

	converter = Converter()
	converter.execute(installationId, dataDirectory)

print 'stop'

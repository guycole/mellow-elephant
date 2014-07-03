#! /usr/bin/python
#
# Title:UploadDatum.py
# Description:Mellow Elephant data upload
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import pickle
import sys
import yaml

from AuthorizeTest import AuthorizeTest
from GetHome import GetHome
from UploadObservation import UploadObservation
from UploadSortie import UploadSortie

class UploadDatum:

	def discoverSorties(self):
		"""
		only directories w/a sortie file are eligible for upload
		"""
		result = []

		directories = os.listdir(self.dataDirectory)
		for directory in directories:
			target = dataDirectory + "/" + directory + "/sortie.p"
			if os.path.isfile(target):
				result.append(target)

		return result

	def writeObservations(self, sortie, observationUrl):
		uploadObservation = UploadObservation()

		targets = os.listdir(sortie.getDirectory(self.dataDirectory))
		for target in targets:
			if target.startswith('observation'):
				fileName = sortie.getDirectory(self.dataDirectory) + "/" + target
				observation = pickle.load(open(fileName, "rb"))

				flag = uploadObservation.execute(observation, sortie, observationUrl)
				if flag:
					os.remove(fileName)
				else:
					print 'observation upload failure'
					return

	def writeSortie(self, sortie, sortieUrl):
		uploadSortie = UploadSortie()

		targetDirectory = sortie.getDirectory(self.dataDirectory)

		targets = os.listdir(targetDirectory)
		if len(targets) == 1:
			flag = uploadSortie.execute(sortie, sortieUrl)
			if flag:
				os.remove(sortie.getPickledSortieName(self.dataDirectory))
				os.rmdir(targetDirectory)
			else:
				print 'sortie upload failure'

	def execute(self, dataDirectory, homeUrl):
		self.dataDirectory = dataDirectory

		getHome = GetHome()
		flag = getHome.execute(homeUrl)
		if flag:
			sortieFiles = self.discoverSorties()
			for sortieFile in sortieFiles:
				sortie = pickle.load(open(sortieFile, "rb"))
				print "current installation:%s" % sortie.installationId
				print "current sortie:%s" % sortie.sortieId

				authorizeTest = AuthorizeTest()
				if authorizeTest.execute(sortie.installationId, getHome.getAuthorizeUrl()):
					self.writeObservations(sortie, getHome.getObservationUrl())
					self.writeSortie(sortie, getHome.getSortieUrl())
				else:
					print 'authorization failure noted'

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

	homeUrl = configuration['homeUrl']
	print homeUrl

	uploadDatum = UploadDatum()
	uploadDatum.execute(dataDirectory, homeUrl)

print 'stop'

#! /usr/bin/python
#
# Title:UploadDatum.py
# Description:Mellow Elephant data upload
# Development Environment:OS X 10.9.3/Python 2.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import sys
import yaml

from AuthorizeTest import AuthorizeTest
from GetHome import GetHome
from Observation import Observation
from Sortie import Sortie
from UploadObservation import UploadObservation
from UploadSortie import UploadSortie

class UploadDatum:

	def execute(self, dataDirectory, installationId, homeUrl):
		getHome = GetHome()
		flag = getHome.execute(homeUrl)
		if flag:
			authorizeTest = AuthorizeTest()
			if authorizeTest.execute(installationId, getHome.getAuthorizeUrl()):
				sortie = Sortie(installationId, 'Default Sortie Name')

				uploadSortie = UploadSortie()
				uploadSortie.execute(sortie, getHome.getSortieUrl())

				observations = []
				observations.append(Observation())
				observations.append(Observation())
				observations.append(Observation())
				observations.append(Observation())

				uploadObservation = UploadObservation()
				flag = uploadObservation.execute(observations, sortie, getHome.getObservationUrl())
				if flag:
					print 'happy ending'

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

	homeUrl = configuration['homeUrl']
	print homeUrl

	uploadDatum = UploadDatum()
	uploadDatum.execute(dataDirectory, installationId, homeUrl)

print 'stop'

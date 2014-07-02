#
# Title:Task.py
# Description:task
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import pickle

from BandBc780 import BandBc780Factory

from Sortie import Sortie

class Task:
	def __init__(self, frequencyBands, receiver, installationId, dataDirectory, homeUrl):
		self.dataDirectory = dataDirectory
		self.installationId = installationId
		self.receiver = receiver
		self.frequencyBands = frequencyBands
		self.homeUrl = homeUrl

	def createSortie(self):
		sortie = Sortie(self.installationId, "default sortieName")
		print "createSortie:%s" % sortie.sortieId

		os.mkdir(sortie.getDirectory(self.dataDirectory))

		return(sortie)

	def execute(self):
		sortie = self.createSortie()

		bandFactory = BandBc780Factory()

		for ndx in self.frequencyBands:
			band = bandFactory.factory(ndx)
			observations = self.receiver.sampleBand(band)
			pickle.dump(observations, open(sortie.getPickledObservationName(self.dataDirectory, ndx), "wb"))

		# write sortie to signal completion
		pickle.dump(sortie, open(sortie.getPickledSortieName(self.dataDirectory), "wb"))

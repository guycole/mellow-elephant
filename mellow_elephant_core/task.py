#
# Title:task.py
# Description:task
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import pickle

from mellow_elephant_core import band_bc780
from mellow_elephant_core import sortie

class Task:
    def __init__(self, frequencyBands, receiver, installationId, dataDirectory):
        self.dataDirectory = dataDirectory
        self.installationId = installationId
        self.receiver = receiver
        self.frequencyBands = frequencyBands

    def createSortie(self):
        currentSortie = sortie.Sortie(self.installationId, "default sortieName")
        print "createSortie:%s" % currentSortie.sortieId

        os.mkdir(currentSortie.getDirectory(self.dataDirectory))

        return currentSortie

    def execute(self):
        currentSortie = self.createSortie()

        bandFactory = band_bc780.BandBc780Factory()

        for ndx in self.frequencyBands:
            band = bandFactory.factory(ndx)
            observations = self.receiver.sampleBand(band)
            pickle.dump(observations, open(currentSortie.getPickledObservationName(self.dataDirectory, ndx), "wb"))

        # write sortie to signal completion
        pickle.dump(currentSortie, open(currentSortie.getPickledSortieName(self.dataDirectory), "wb"))

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

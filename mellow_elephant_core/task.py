#
# Title:task.py
# Description:
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import pickle

from mellow_elephant_core import band_bc780
from mellow_elephant_core import sortie

class Task:
    def __init__(self, frequencyBands, receiver, dataDirectory):
        self.frequencyBands = frequencyBands
        self.receiver = receiver
        self.dataDirectory = dataDirectory

    def createSortie(self):
        currentSortie = sortie.Sortie("default sortieName")
        print "createSortie:%s" % currentSortie.sortieId

        os.mkdir(currentSortie.getDirectory(self.dataDirectory))

        return currentSortie

    def execute(self):
        """
        visit each frequency band and write observation files
        """
        bandFactory = band_bc780.BandBc780Factory()

        currentSortie = self.createSortie()
        for ndx in self.frequencyBands:
            band = bandFactory.factory(ndx)
            observations = self.receiver.sampleBand(band)
            pickle.dump(observations, open(currentSortie.getPickledObservationName(self.dataDirectory, ndx.bandNdx), "wb"))

        # write sortie to signal completion
        pickle.dump(currentSortie, open(currentSortie.getPickledSortieName(self.dataDirectory), "wb"))

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

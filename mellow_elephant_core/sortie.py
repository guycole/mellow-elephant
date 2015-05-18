#
# Title:sortie.py
# Description:sortie utilities
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import time
import uuid


class Sortie:
    def __init__(self, sortieName):
        self.sortieId = str(uuid.uuid4())
        self.sortieName = sortieName
        self.timeStampMs = int(1000 * time.time())

    def toDictionary(self):
        result = {}
        result['sortieId'] = self.sortieId
        result['sortieName'] = self.sortieName
        result['timeStampMs'] = self.timeStampMs
        return result

    def getDirectory(self, dataDirectory):
        return dataDirectory + "/" + self.sortieId

    def getPickledSortieName(self, dataDirectory):
        return dataDirectory + "/" + self.sortieId + "/sortie.p"

    def getPickledObservationName(self, dataDirectory, bandNdx):
        filename = "/observation%d.p" % bandNdx
        return dataDirectory + "/" + self.sortieId + filename

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
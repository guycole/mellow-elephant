#
# Title:Sortie.py
# Description:sortie container
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

import time
import uuid

from datetime import datetime

class Sortie:
	def __init__(self, installationId, sortieName):
		self.installationId = installationId
		self.sortieId = str(uuid.uuid4())
		self.sortieName = sortieName
		self.timeStampMs = int(1000 * time.time())

	def toDictionary(self):
		result = {}
		result['sortieId'] = self.sortieId
		result['sortieName'] = self.sortieName
		result['timeStampMs'] = self.timeStampMs
		result['installationId'] = self.installationId
		return(result)

	def getDirectory(self, dataDirectory):
		return dataDirectory + "/" + self.sortieId

	def getPickledSortieName(self, dataDirectory):
		return dataDirectory + "/" + self.sortieId + "/sortie.p"

	def getPickledObservationName(self, dataDirectory, bandNdx):
		filename = "/observation%d.p" % bandNdx
		return dataDirectory + "/" + self.sortieId + filename

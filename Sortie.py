#
# Title:Sortie.py
# Description:sortie container
# Development Environment:OS X 10.9.3/Python 2.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import uuid

from datetime import datetime

class Sortie:
	def __init__(self, installationId, sortieName):
		self.installationId = installationId
		self.sortieId = str(uuid.uuid4())
		self.sortieName = sortieName
		self.timeStampMs = 1000 * int((datetime.utcnow()-datetime(1970,1,1)).total_seconds())

	def toDictionary(self):
		result = {}
		result['sortieId'] = self.sortieId
		result['sortieName'] = self.sortieName
		result['timeStampMs'] = self.timeStampMs
		result['installationId'] = self.installationId
		return(result)
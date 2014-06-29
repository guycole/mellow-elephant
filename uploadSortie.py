#
# Title:UploadSortie.py
# Description:Mellow Elephant
# Development Environment:OS X 10.9.3/Python 2.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import json
import urllib2

class UploadSortie:

	def execute(self, sortie, sortieUrl):
		"""
			upload sortie
		"""
		payload = json.dumps(sortie.toDictionary())

		headers = {'Accept':'application/json', 'Content-Type':'application/json;charset=UTF-8'}

		request = urllib2.Request(sortieUrl, payload, headers)

		try:
			response = urllib2.urlopen(request)
			result = json.loads(response.read())
			response.close()

			if result['status'] == 'OK':
				return True
		except urllib2.HTTPError:
			print 'UploadSortie exception:' + sortieUrl

		return False
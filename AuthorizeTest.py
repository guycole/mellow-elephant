#
# Title:AuthorizeTest.py
# Description:discover if this installation is on the white list
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import json
import urllib2

class AuthorizeTest:

	def execute(self, installationId, authorizeUrl):
		"""
			discover if this installation is on the white list
		"""
		message = {}
		message['installationId'] = installationId
		payload = json.dumps(message)

		headers = {'Accept':'application/json', 'Content-Type':'application/json;charset=UTF-8'}

		request = urllib2.Request(authorizeUrl, payload, headers)

		try:
			response = urllib2.urlopen(request)
			result = json.loads(response.read())
			response.close()

			if result['status'] == 'OK':
				return True
		except urllib2.HTTPError:
			print 'AuthorizeTest exception:' + authorizeUrl

		return False

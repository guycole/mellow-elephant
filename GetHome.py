#
# Title:GetHome.py
# Description:read home URL for configuration
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import json
import urllib2

class GetHome:

	def execute(self, url):
		"""
			read home configuration and extract links
			return True on success
		"""
		self.authorizeUrl = 'unknown'
		self.observationUrl = 'unknown'
		self.sortieUrl = 'unknown'

		try:
			result = json.load(urllib2.urlopen(url))

			links = result['_links']

			authorize = links['authorize']
			self.authorizeUrl = authorize['href']

			observation = links['observation']
			self.observationUrl = observation['href']

			sortie = links['sortie']
			self.sortieUrl = sortie['href']

			return True
		except urllib2.HTTPError:
			print 'GetHome exception:' + url

		return False

	def getAuthorizeUrl(self):
		"""
			return authorization url
		"""
		return(self.authorizeUrl)

	def getObservationUrl(self):
		"""
		  return observation url
		"""
		return(self.observationUrl)

	def getSortieUrl(self):
		"""
		  return sortie url
		"""
		return(self.sortieUrl)

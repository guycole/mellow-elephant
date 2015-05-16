#
# Title:ReceiverFactory.py
# Description:create receiver based on type
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import bc780

class ReceiverFactory:

	def factory(self, receiverType, receiverProxy):
		if receiverType == 'bc780':
			print 'receiver bc780 selected'
			return bc780.ReceiverBc780(receiverProxy)
		else:
			print "unknown receiverType:%s" % self.receiverType
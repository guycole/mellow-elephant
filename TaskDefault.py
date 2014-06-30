#
# Title:TaskDefault.py
# Description:default task
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
from Task import Task

class TaskDefault(Task):

	def __init__(self, receiver):
		Task.__init__(self, 'default', receiver)
		print 'task default ctor'

	def __str__(self):
		return self.taskType

	def execute(self):
		print 'execute'
		ndx = 0
		limit = 10
		while ndx < limit:
			ndx += 1
			print 'forloop'
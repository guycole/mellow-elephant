#
# Title:Task.py
# Description:task parent
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

class Task:
	def __init__(self, taskType, receiver):
		print 'task ctor'
		self.taskType = taskType
		self.receiver = receiver

	def __str__(self):
		return self.taskType

	def execute(self):
		print 'execute'
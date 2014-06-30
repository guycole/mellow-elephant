#
# Title:TaskFactory.py
# Description:create task based on type
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import TaskDefault

class TaskFactory:

	def factory(self, taskType, receiver):
		if taskType == 'default':
			return TaskDefault.TaskDefault(receiver)
		else:
			print "unknown taskType:%s" % self.taskType
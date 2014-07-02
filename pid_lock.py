#
# Title:pid_lock.py
# Description:ensure only a single instance runs
# Development Environment:Ubuntu 10.04 LTS/Python 2.6.5
# Legalise:Copyright (C) 2013 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os

class PidLock:

    def lockTest(self, file_name):
        """
        Return True if active lock noted
        """
        try:
            infile = open(file_name, 'r')
            target_pid = int(infile.readline())
            infile.close()
        except IOError:
            return False

#        target_pid = os.getpid()

        command = "/bin/ps -p %d --no-headers" % (target_pid)
        temp = os.popen(command).readlines()

        if (len(temp) > 0):
            return True

        return False

    def writeLock(self, file_name):
        """
        write a PID lock file
        """
        outfile = open(file_name, 'w')
        outfile.write("%d\n" % (os.getpid()))
        outfile.close()

#
#
#
if __name__ == '__main__':
    print 'start'

    pidLock = PidLock()
    flag = pidLock.lockTest('/tmp/target')
    print flag

    if flag:
        print 'flag true'
    else:
        print 'flag false'
        pidLock.writeLock('/tmp/target')

    print 'stop'

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***

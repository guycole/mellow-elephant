#
# Title:test_pidlock.py
# Description:exercise pidlock
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import unittest

from mellow_elephant_core import pid_lock

class MyTestCase(unittest.TestCase):
    def test_0(self):
        pidLock = pid_lock.PidLock()
        assert not pidLock.lockTest('/tmp/target')
        pidLock.writeLock('/tmp/target')
#        assert pidLock.lockTest('/tmp/target')

if __name__ == '__main__':
    unittest.main()

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
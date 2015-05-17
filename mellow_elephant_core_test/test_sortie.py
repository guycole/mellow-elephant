#
# Title:test_sortie.py
# Description:exercise sortie model
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import unittest

from mellow_elephant_core import sortie

class MyTestCase(unittest.TestCase):
    def test_0(self):
        testx = sortie.Sortie('installationId', 'sortieName')
        dataDirectory = testx.toDictionary()
#        assert testx.getDirectory("/tmp") == '/tmp/ff28befc-39bf-40e6-9774-6f718baeb645'
#        assert testx.getPickledSortieName("/tmp") == '/tmp/ff28befc-39bf-40e6-9774-6f718baeb645/sortie.p'
#        assert testx.getPickledObservationName("/tmp", 10) == '/tmp/ff28befc-39bf-40e6-9774-6f718baeb645/observation10.p'

if __name__ == '__main__':
    unittest.main()

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
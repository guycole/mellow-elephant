#
# Title:test_band_bc780.py
# Description:exercise band definitions
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import unittest

from mellow_elephant_core import band_bc780

class MyTestCase(unittest.TestCase):
    def test_0(self):
        bc780 = band_bc780.BandBc780Factory()
        assert bc780.matcher(100.0 * 10000) == 10

    def test_1(self):
        bc780 = band_bc780.BandBc780Factory()
        selectedBand = bc780.factory(10)

        assert selectedBand.bandNdx == 10
        assert selectedBand.frequencyLow == 88.0
        assert selectedBand.frequencyHigh == 107.9
        assert selectedBand.frequencyStep == 100.0
        assert selectedBand.modulation == 'WFM'
#
if __name__ == '__main__':
    unittest.main()

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
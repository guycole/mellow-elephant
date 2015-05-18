#
# Title:test_receiver.py
# Description:exercise receiver model
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import unittest

from mellow_elephant_core import receiver

class MyTestCase(unittest.TestCase):
    def test_0(self):
        testx = receiver.Receiver('rxType', 'rxProxy')
        assert testx.receiverProxy == 'rxProxy'
        assert testx.receiverType == 'rxType'
        assert testx.testRadio() is False

    def test_1(self):
        testx = receiver.ReceiverBc780('rxProxy')
        assert testx.receiverProxy == 'rxProxy'
        assert testx.receiverType == 'bc780'
        assert testx.testRadio() is False

    def test_2(self):
        testx = receiver.ReceiverStub('rxProxy')
        assert testx.receiverProxy == 'rxProxy'
        assert testx.receiverType == 'stub'
        assert testx.testRadio() is True
        assert testx.tuneRadio(1234567890)
        assert testx.getModulation() == 'XX'

        rawSample = testx.getRawSample()
        assert rawSample[0] == 123
        assert rawSample[1] == 1234567890

if __name__ == '__main__':
    unittest.main()

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
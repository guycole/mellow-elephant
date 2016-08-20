#! /usr/bin/python
#
# Title:bc780_test.py
# Description: exercise receiver
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#ds
import sys
import yaml

from receiver import ReceiverFactory

class Bc780Test:

    def execute(self):
        receiver_factory = ReceiverFactory()
        current_receiver = receiver_factory.factory(receiver_type, receiver_proxy)

#./sampler1 AF
#./sampler1 AL
#./sampler1 AR
#./sampler1 AT
#./sampler1 BA
#./sampler1 BP
#./sampler1 BT
#./sampler1 CB
#./sampler1 CC
#./sampler1 CD
#./sampler1 CS
#./sampler1 CT
#./sampler1 DT
#./sampler1 DL
#./sampler1 DS
#./sampler1 EL
#./sampler1 FB
#./sampler1 FI
#./sampler1 FI
#./sampler1 FP
#./sampler1 IC
#./sampler1 ID
#./sampler1 IL
#./sampler1 IR
#./sampler1 IS
#./sampler1 KEY
#./sampler1 LCD
#./sampler1 LL
#./sampler1 LM
#./sampler1 LO
#./sampler1 LT
#./sampler1 LU
#./sampler1 MA
#./sampler1 MD
#./sampler1 MD01
#./sampler1 MD
#./sampler1 MD
#./sampler1 MU
#./sampler1 PC
#./sampler1 PI
#./sampler1 PM
#./sampler1 PR
#./sampler1 QU
#./sampler1 RF01198000?
#./sampler1 RG
#./sampler1 RI
#./sampler1 RM
#./sampler1 SB
#./sampler1 SG
#./sampler1 SI
#./sampler1 SQ
#./sampler1 SS
#./sampler1 ST
#./sampler1 TA
#./sampler1 TB
#./sampler1 TC
#./sampler1 TD
#./sampler1 TG
#./sampler1 TR
#./sampler1 VR
#./sampler1 WA
#./sampler1 WI
#./sampler1 SG
#./sampler1 RF01241000?
#./sampler1 SG
#./sampler1 WI

print 'start'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        fileName = "config.yaml"

    configuration = yaml.load(file(fileName))

    receiver_type = configuration['receiverType']
    receiver_proxy = configuration['receiverProxy']

    driver = Bc780Test()
    driver.execute()

print 'stop'

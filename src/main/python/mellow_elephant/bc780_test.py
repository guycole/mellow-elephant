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
        current_receiver = receiver_factory.factory(receiver_type, serial_device)

        result = current_receiver.invoke_radio('SI', '')
        print result

        result = current_receiver.invoke_radio('AF', '')
        print result

        result = current_receiver.invoke_radio('AL', '')
        print result

        result = current_receiver.invoke_radio('AR', '')
        print result

        result = current_receiver.invoke_radio('AT', '')
        print result

        result = current_receiver.invoke_radio('BA', '')
        print result

        result = current_receiver.invoke_radio('BP', '')
        print result

        result = current_receiver.invoke_radio('BT', '')
        print result

        result = current_receiver.invoke_radio('CB', '')
        print result

        result = current_receiver.invoke_radio('CC', '')
        print result

        result = current_receiver.invoke_radio('CD', '')
        print result

        result = current_receiver.invoke_radio('CS', '')
        print result

        result = current_receiver.invoke_radio('CT', '')
        print result

        result = current_receiver.invoke_radio('DT', '')
        print result

        result = current_receiver.invoke_radio('DL', '')
        print result

        result = current_receiver.invoke_radio('DS', '')
        print result

        result = current_receiver.invoke_radio('EL', '')
        print result

        result = current_receiver.invoke_radio('FB', '')
        print result

        result = current_receiver.invoke_radio('FI', '')
        print result

        result = current_receiver.invoke_radio('FP', '')
        print result

        result = current_receiver.invoke_radio('IC', '')
        print result

        result = current_receiver.invoke_radio('ID', '')
        print result

        result = current_receiver.invoke_radio('IL', '')
        print result

        result = current_receiver.invoke_radio('IR', '')
        print result

        result = current_receiver.invoke_radio('IS', '')
        print result

        result = current_receiver.invoke_radio('KEY', '')
        print result

        result = current_receiver.invoke_radio('LCD', '')
        print result

        result = current_receiver.invoke_radio('LL', '')
        print result

        result = current_receiver.invoke_radio('LM', '')
        print result

        result = current_receiver.invoke_radio('LO', '')
        print result

        result = current_receiver.invoke_radio('LT', '')
        print result

        result = current_receiver.invoke_radio('LU', '')
        print result

        result = current_receiver.invoke_radio('MA', '')
        print result

        result = current_receiver.invoke_radio('MD', '')
        print result

        result = current_receiver.invoke_radio('MD', '01')
        print result

        result = current_receiver.invoke_radio('MU', '')
        print result

        result = current_receiver.invoke_radio('PC', '')
        print result

        result = current_receiver.invoke_radio('PI', '')
        print result

        result = current_receiver.invoke_radio('PM', '')
        print result

        result = current_receiver.invoke_radio('PR', '')
        print result

        result = current_receiver.invoke_radio('QU', '')
        print result

        result = current_receiver.invoke_radio('RF', '01198000?')
        print result

        result = current_receiver.invoke_radio('RG', '')
        print result

        result = current_receiver.invoke_radio('RI', '')
        print result

        result = current_receiver.invoke_radio('RM', '')
        print result

        result = current_receiver.invoke_radio('SB', '')
        print result

        result = current_receiver.invoke_radio('SG', '')
        print result

        result = current_receiver.invoke_radio('SI', '')
        print result

        result = current_receiver.invoke_radio('SQ', '')
        print result

        result = current_receiver.invoke_radio('SS', '')
        print result

        result = current_receiver.invoke_radio('ST', '')
        print result

        result = current_receiver.invoke_radio('TA', '')
        print result

        result = current_receiver.invoke_radio('TB', '')
        print result

        result = current_receiver.invoke_radio('TC', '')
        print result

        result = current_receiver.invoke_radio('TD', '')
        print result

        result = current_receiver.invoke_radio('TG', '')
        print result

        result = current_receiver.invoke_radio('TR', '')
        print result

        result = current_receiver.invoke_radio('VR', '')
        print result

        result = current_receiver.invoke_radio('WA', '')
        print result

        result = current_receiver.invoke_radio('WI', '')
        print result

        result = current_receiver.invoke_radio('SG', '')
        print result

        result = current_receiver.invoke_radio('RF', '01241000?')
        print result

        result = current_receiver.invoke_radio('SG', '')
        print result

        result = current_receiver.invoke_radio('WI', '')
        print result

        result = current_receiver.test_radio()
        print result

        result = current_receiver.get_modulation()
        print result

        result = current_receiver.get_raw_sample()
        print result

        result = current_receiver.sample_radio(4567890)
        print result

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
    print "receiver type:%s" % receiver_type

    serial_device = configuration['serialDevice']
    print "serial device:%s" % serial_device

    driver = Bc780Test()
    driver.execute()

print 'stop'

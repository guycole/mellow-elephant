#
# Title:receiver.py
# Description:radio receiver classes
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import random
#import serial
import time

from observation import Observation

class ReceiverFactory:
    def factory(self, receiver_type, serial_device):
        if receiver_type == 'bc780':
            return ReceiverBc780(serial_device)
        elif receiver_type == 'stub':
            return ReceiverStub(serial_device)
        else:
            print("unknown receiverType:%s" % self.receiver_type)


class Receiver:
    def __init__(self, receiver_type, serial_device):
        self.receiver_type = receiver_type
        self.serial_device = serial_device

    def __str__(self):
        buffer = "%s:%s" % (self.receiver_type, self.serial_device)
        return buffer

    def invoke_radio(self, command, argz):
        """
        invoke the external command line utility and return response
        """
        return 'bogus'

    def test_radio(self):
        """
        return true if radio is enabled and active
        """
        return False

    def tune_radio(self, frequency):
        """
        tune radio frequency
        """
        return frequency

    def get_modulation(self):
        """
        return current modulation mode
        """
        return 'XX'

    def get_raw_sample(self):
        """
        return current audio sample
        """
        return [123, 1234567890]

    def sample_band(self, band):
        """
        sample an entire frequency band
        return collection of observations
        """
        result_list = []
        step_frequency = band.frequency_step / 1000.0
        current_frequency = band.frequency_low
        limit_frequency = band.frequency_high + step_frequency
        while current_frequency < limit_frequency:
            tweaked_frequency = int(round(current_frequency * 10000))
            sample = self.sample_radio(tweaked_frequency)
            current_observation = Observation(sample[0], sample[1])
            result_list.append(current_observation)
            current_frequency += step_frequency

        return result_list

class ReceiverStub(Receiver):
    def __init__(self, receiver_proxy):
        Receiver.__init__(self, 'stub', receiver_proxy)

    def test_radio(self):
        return True

    def sample_radio(self, frequency):
        """
        tune to frequency and sample signal strength
        return tuple of frequency, strength and modulation
        """
        return [frequency, random.randrange(1, 255), 'XX']

class ReceiverBc780(Receiver):
    def __init__(self, serial_device):
        Receiver.__init__(self, 'bc780', serial_device)
#        self.port = serial.Serial(serial_device, baudrate=9600, timeout=1.0)

    def invoke_radio(self, command, argz):
        """
        send command to radio and wait for response
        """
        tx_buffer = "\r\n%s%s\r\n" % (command, argz)
        self.port.write(tx_buffer)

        rx_buffer = ''
        
        while True:
            raw_buffer = self.port.read(15)
            if len(raw_buffer) < 1:
                break
            else:
                rx_buffer += raw_buffer

        return rx_buffer.strip()

    def test_radio(self):
        """
        return true if the radio is awake and responsive
        """
        result = self.invoke_radio('SI', '')
        print("::%s::" % result)

        try:
            ndx1 = result.index('BC780XLT')
            return True
        except ValueError:
            return False

    def tune_radio(self, frequency):
        """
        tune scanner to specified frequency
        returns frequency as integer
        """
        argz = "%8.8d?" % frequency
        result = self.invoke_radio('RF', argz)
        return result[2:]

    def get_modulation(self):
        """
        return current modulation mode
        """
        result = self.invoke_radio('RM', '')
        ndx1 = result.rindex(' ')
        return result[ndx1+1:]

    def get_raw_sample(self):
        """
        return current sample (signal strength and integer frequency)
        """
        result = self.invoke_radio('SG', '')

        ndx1 = result.rindex('S')
        ndx2 = result.index(' ', ndx1)
        strength = result[ndx1+1:ndx2]

        ndx1 = result.rindex('F')
        frequency = result[ndx1+1:]

        return [int(strength), long(frequency)]

    def sample_radio(self, frequency):
        """
        tune to frequency and sample signal strength
        return tuple of frequency, strength and modulation
        """
        self.tune_radio(frequency)

        modulation = self.get_modulation()

        sample = self.get_raw_sample()

        return [sample[0], sample[1], modulation]

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

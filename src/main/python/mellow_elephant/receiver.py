#
# Title:receiver.py
# Description:radio receiver classes
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import random
import time

from observation import Observation

class ReceiverFactory:
    def factory(self, receiver_type, receiver_proxy):
        if receiver_type == 'bc780':
            return ReceiverBc780(receiver_proxy)
        elif receiver_type == 'stub':
            return ReceiverStub(receiver_proxy)
        else:
            print "unknown receiverType:%s" % self.receiver_type


class Receiver:
    def __init__(self, receiver_type, receiver_proxy):
        self.receiver_type = receiver_type
        self.receiver_proxy = receiver_proxy

    def __str__(self):
        buffer = "%s:%s" % (self.receiver_type, self.receiver_proxy)
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
        return collection of samples
        """
        result_list = []
        step_frequency = band.frequency_step / 1000.0
        current_frequency = band.frequency_low
        limit_frequency = band.frequency_high + step_frequency
        while current_frequency < limit_frequency:
            tweaked_frequency = int(round(current_frequency * 10000))
            sample = self.get_raw_sample(tweaked_frequency)
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
    def __init__(self, receiver_proxy):
        Receiver.__init__(self, 'bc780', receiver_proxy)

    def invoke_radio(self, command, argz):
        """
        invoke the external command line utility and return response
        """
        command_line = "%s %s%s" % (self.receiver_proxy, command, argz)

        temp1 = os.popen(command_line).readlines()
        if len(temp1) == 0:
            return 'NONE'

        temp2 = temp1[0]

        try:
            ndx1 = temp2.rindex(command)
            ndx2 = temp2.index('\n', ndx1)
            return(temp2[ndx1:ndx2])
        except ValueError:
            return 'NONE'

    def test_radio(self):
        """
        return true if the radio is awake and responsive
        """
        result = self.invoke_radio('SI', '')
        print "::%s::" % result

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
        argz = "%8.8d?" % (frequency)

        exit_flag = False
        error_counter = 0

        while ((exit_flag is False) and (error_counter < 10)):
            result = self.invoke_radio('RF', argz)

            if result == 'NONE':
                print '--------------->receiver tune parse error noted'
                time.sleep(1)
                error_counter += 1
            else:
                return(result[2:])

        print '--------------->receiver tune errors exceed retry limit'
        return 0

    def get_modulation(self):
        """
        return current modulation mode
        """
        exit_flag = False
        error_counter = 0

        while ((exit_flag is False) and (error_counter < 10)):
            result = self.invoke_radio('RM', '')

            if result == 'NONE':
                print '--------------->receiver modulation parse error noted'
                time.sleep(1)
                error_counter += 1
            else:
                return(result[3:])

        print '--------------->receiver modulation errors exceed retry limit'
        return 'NONE'

    def get_raw_sample(self):
        """
        return current sample (signal strength and integer frequency)
        """
        exit_flag = False
        error_counter = 0

        command = "%s SG" % (self.receiver_proxy)

        while ((exit_flag is False) and (error_counter < 10)):
            temp1 = os.popen(command).readlines()
            temp2 = temp1[0]

            try:
                ndx1 = temp2.rindex('S')
                ndx2 = temp2.index(' ', ndx1)
                strength = temp2[ndx1+1:ndx2]

                ndx1 = temp2.rindex('F')
                ndx2 = temp2.index('\n', ndx1)
                frequency = temp2[ndx1+1:ndx2]

                return [int(strength), long(frequency)]
            except ValueError:
                print '--------------->receiver sample parse error noted'
                print command
                print temp1

            time.sleep(1)
            error_counter += 1

        print '--------------->receiver sample errors exceed retry limit'
        return [0, 0]

    def sample_radio(self, frequency):
        """
        tune to frequency and sample signal strength
        return tuple of frequency, strength and modulation
        """
        time.sleep(1)
        tune_status = self.tune_radio(frequency)
        if tune_status < 1:
            print 'tune failure'

        time.sleep(1)
        modulation = self.get_modulation()

        time.sleep(1)
        sample = self.get_raw_sample()

        return [sample[0], sample[1], modulation]

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

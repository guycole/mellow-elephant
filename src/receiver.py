#
# Title:receiver.py
# Description:radio receiver classes
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import logging
import serial
import time

from band_bc780 import BandBc780Factory


class ReceiverFactory:
    def __init__(self):
        self.logger = logging.getLogger()

    def factory(self, receiver_type, serial_device):
        self.logger.info("receiver factory:%s" % receiver_type)

        if receiver_type == "bc780":
            return ReceiverBc780(serial_device)
        #        elif receiver_type == 'rtlsdr':
        #            pass
        #            return ReceiverRtlSdr(serial_device)
        #        elif receiver_type == 'stub':
        #            pass
        #            return ReceiverStub(serial_device)
        else:
            print("unknown receiverType:%s" % self.receiver_type)


class Receiver:
    def __init__(self, receiver_type, serial_device):
        self.logger = logging.getLogger()

        self.receiver_type = receiver_type
        self.serial_device = serial_device

        self.band_factory = BandBc780Factory()

    def __str__(self):
        buffer = "%s:%s" % (self.receiver_type, self.serial_device)
        return buffer

    def invoke_radio(self, command, argz):
        """
        invoke the external command line utility and return response
        """
        return "bogus"

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
        return "XX"

    def get_raw_sample(self):
        """
        return current audio sample
        """
        return [123, 1234567890]


class ReceiverBc780(Receiver):
    def __init__(self, serial_device):
        Receiver.__init__(self, "bc780", serial_device)
        self.port = serial.Serial(serial_device, baudrate=9800, timeout=1.0)

    def invoke_radio(self, command: str, argz: str) -> str:
        """
        send command to radio and wait for response
        """
        tx_buffer = "%s%s\r" % (command, argz)
        #        print(f"tx_buffer {tx_buffer}")

        self.port.write(tx_buffer.encode())

        rx_buffer = ""

        while True:
            raw_buffer = self.port.read(15)
            if len(raw_buffer) < 1:
                break
            else:
                rx_buffer += str(raw_buffer)

        #        print(rx_buffer)

        return rx_buffer.strip()

    def test_radio(self) -> bool:
        """
        return true if the radio is awake and responsive
        """
        #
        self.logger.debug("test_radio")

        result = self.invoke_radio("SI", "")

        ndx1 = result.find("BC780XLT")
        if ndx1 < 0:
            return False
        else:
            return True

    def tune_radio(self, frequency: int) -> str:
        """
        tune scanner to specified frequency
        returns frequency as integer
        """
        self.logger.debug("tune_radio")

        argz = "%8.8d" % frequency
        result = self.invoke_radio("RF", argz)
        return result

    def get_modulation(self):
        """
        return current modulation mode
        """
        self.logger.debug("get_modulation")

        result = self.invoke_radio("RM", "")

        ndx1 = result.find(" ")
        ndx2 = len(result)

        return result[ndx1 + 1 : ndx2 - 3]

    def get_raw_sample(self):
        """
        return current sample (signal strength and integer frequency)
        """
        self.logger.debug("get_raw_sample")

        result = self.invoke_radio("SG", "")

        ndx1 = result.find(" ")
        ndx2 = len(result)

        strength = result[3:ndx1]
        frequency = result[ndx1 + 2 : ndx2 - 3]
        return (int(strength), int(frequency))

    def sample_radio(self, frequency: int):
        """
        tune to frequency and sample signal strength
        return tuple of frequency, strength and modulation
        """
        retstat = self.tune_radio(frequency)
        if retstat.find("OK") > 0:
            self.logger.debug(f"radio tune OK {frequency}")
        else:
            self.logger.debug(f"radio tune failure {frequency}")
            return None

        modulation = self.get_modulation()

        sample = self.get_raw_sample()

        return (sample[0], sample[1], modulation, int(time.time()))

    def sample_band(self, band_ndx):
        """
        sample an entire frequency band
        return collection of observations
        """
        frequency_band = self.band_factory.factory(band_ndx)

        counter = 0

        result_list = []
        step_frequency = frequency_band.frequency_step / 1000.0
        current_frequency = frequency_band.frequency_low
        limit_frequency = frequency_band.frequency_high + step_frequency
        while current_frequency < limit_frequency:
            tweaked_frequency = int(round(current_frequency * 10000))
            sample = self.sample_radio(tweaked_frequency)
            if sample is not None:
                print(sample)
                result_list.append(sample)

                counter += 1
                if counter > 5:
                    return result_list

            current_frequency += step_frequency

        return result_list


# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

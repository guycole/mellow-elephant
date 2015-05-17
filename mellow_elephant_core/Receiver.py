#
# Title:receiver.py
# Description:radio receiver classes
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import time


class ReceiverFactory:
    def factory(self, receiverType, receiverProxy):
        receiver = Receiver(receiverType, receiverProxy)
        if receiverType == 'bc780':
            return ReceiverBc780(receiver)
        else:
            print "unknown receiverType:%s" % self.receiverType


class Receiver:
    def __init__(self, receiverType, receiverProxy):
        self.receiverType = receiverType
        self.receiverProxy = receiverProxy

    def __str__(self):
        return self.receiverType


class ReceiverBc780(Receiver):
    def __init__(self, receiverProxy):
        Receiver.__init__(self, 'bc780', receiverProxy)

    def invokeRadio(self, command, argz):
        """
        invoke the external command line utility and return response
        """
        commandLine = "%s %s%s" % (self.receiverProxy, command, argz)
        print commandLine

#        temp1 = os.popen(commandLine).readlines()
#        temp2 = temp1[0]
#
#        try:
#            ndx1 = temp2.rindex(command)
#            ndx2 = temp2.index('\n', ndx1)
#            return(temp2[ndx1:ndx2])
#        except ValueError:
#            return("NONE")

    def testRadio(self):
        """
        return true if the radio is awake and responsive
        """
        result = self.invokeRadio("SI", "")
        print "::%s::" % result

        try:
            ndx1 = result.index("BC780XLT")
            return True
        except ValueError:
            return False

    def tuneRadio(self, frequency):
        """
        tune scanner to specified frequency
        returns frequency as integer
        """
        argz = "%8.8d?" % (frequency)

        exitFlag = False
        errorCounter = 0

        while ((exitFlag is False) and (errorCounter < 10)):
            result = self.invokeRadio("RF", argz)
            print result

        if result == 'NONE':
            print "--------------->receiver tune parse error noted"
            time.sleep(1)
            errorCounter += 1
        else:
            return(result[2:])

        print "--------------->receiver tune errors exceed retry limit"
        return 0

    def getModulation(self):
        """
        return current modulation mode
        """
        exitFlag = False
        errorCounter = 0

        while ((exitFlag is False) and (errorCounter < 10)):
            result = self.invokeRadio("RM", "")

        if result == 'NONE':
            print "--------------->receiver modulation parse error noted"
            time.sleep(1)
            errorCounter += 1
        else:
            return(result[3:])

        print "--------------->receiver modulation errors exceed retry limit"
        return("NONE")

    def getRawSample(self):
        """
        return current sample (signal strength and integer frequency)
        """
        exitFlag = False
        errorCounter = 0

        command = "%s SG" % (self.receiverProxy)

        while ((exitFlag is False) and (errorCounter < 10)):
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
            print "--------------->receiver sample parse error noted"
            print command
            print temp2

            time.sleep(1)
            errorCounter += 1

        print "--------------->receiver sample errors exceed retry limit"
        return [0, 0]

    def sampleRadio(self, frequency):
        """
        tune to frequency and sample signal strength
        return tuple of frequency, strength and modulation
        """
        time.sleep(1)
        self.tuneRadio(frequency)

        time.sleep(1)
        modulation = self.getModulation()

        time.sleep(1)
        sample = self.getRawSample()

        return [sample[1], sample[0], modulation]

    def sampleBand(self, band):
        """
        sample an entire frequency band
        return collection of samples
        """
        stepFrequency = band.frequencyStep / 1000.0
        currentFrequency = band.frequencyLow

#        while currentFrequency < band.frequencyHigh:
        sample = self.sampleRadio(currentFrequency)
#            currentFrequency = currentFrequency + stepFrequency

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

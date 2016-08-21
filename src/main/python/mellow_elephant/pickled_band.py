#
# Title:pickled_band.py
# Description: persisted band
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import datetime
import time

class PickledBand:
    def __init__(self, installation, band_ndx, observations):
        self.installation = installation
        self.band_ndx = band_ndx
        self.observations = observations
        self.create_time = int(time.time())

    def get_filename(self, directory):
        time2 = datetime.datetime.utcfromtimestamp(self.create_time)
        time3 = time2.timetuple()
        file_name = "%4.4d_%2.2d_%2.2d_%2.2d_%2.2d_%2.2d" % (time3[0], time3[1], time3[2], time3[3], time3[4], self.band_ndx)
        full_name = "%s/%s" % (directory, file_name)
        return full_name

    def to_dictionary(self):
        result = {}
        result['installation'] = self.installation
        result['band_ndx'] = self.band_ndx
        result['observations'] = self.observations
        result['create_time'] = self.create_time
        return result

#
# Title:pickled_band.py
# Description: JSON persisted band (no longer uses Python pickle)
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import json
import logging
import time
import uuid


class PickledBand:
    def __init__(self, installation, band_ndx, observations):
        self.logger = logging.getLogger()

        self.installation = installation
        self.band_ndx = band_ndx
        self.observations = observations
        self.create_time = int(time.time())
        self.version = 1

    def get_filename(self, directory):
        file_name = "%s/%s-%02d.json" % (directory, self.create_time, self.band_ndx)
        self.logger.info("fresh pickle file:%s" % file_name)
        return file_name

    @property
    def to_json(self) -> str:
        """
        convert all the collected observations to json and add a header
        :return: observations as serialized json
        """
        ma_average = 0
        ma_buffer = []
        ma_length = 71
        ma_sum = 0

        observation_list = []
        for observation in self.observations:
            #
            # moving average calculates noise floor
            # peaks above moving average indicate a radio transmitter
            #
            if len(ma_buffer) > ma_length:
                ma_buffer.pop(0)

            ma_buffer.append(observation[0])
            ma_sum = sum(ma_buffer)
            ma_average = int(ma_sum / len(ma_buffer))

            element = {
                "strength": observation[0],
                "frequency": observation[1],
                "modulation": observation[2],
                "time_stamp": observation[3],
                "moving_average": ma_average,
                "peaker": 1 if observation[0] > (ma_average + 10) else 0,
            }

            observation_list.append(element)

        temp = {}
        temp["band_ndx"] = self.band_ndx
        temp["create_time"] = self.create_time
        temp["installation"] = self.installation
        temp["observations"] = observation_list
        temp["sortie"] = str(uuid.uuid4())
        temp["version"] = self.version

        return json.dumps(temp)

#
# Title:pickled_band.py
# Description: persisted band
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
        file_name = f"{directory}/{self.create_time}-{self.band_ndx:02d}.json"
        self.logger.info(f"fresh pickle file:{file_name}")
        return file_name

    def to_json(self) -> str:
        """
        convert all the collected observations to json and add a header
        :return: observations as serialized json
        """
        ma_average = 0
        ma_buffer = []
        ma_length = 5
        ma_sum = 0

        observation_list = []
        for observation in self.observations:
            if len(ma_buffer) > ma_length:
                ma_buffer.pop(0)

            ma_buffer.append(observation[0])
            ma_sum = sum(ma_buffer)
            ma_average = int(ma_sum/len(ma_buffer))

            element = {
                'strength': observation[0],
                'frequency': observation[1],
                'modulation': observation[2],
                'timestamp': observation[3],
                'moving_average': ma_average,
                'peaker': True if observation[0] > (ma_average * 1.3) else False
            }
            observation_list.append(element)

        temp = {}
        temp['band_ndx'] = self.band_ndx
        temp['create_time'] = self.create_time
        temp['installation'] = self.installation
        temp['observations'] = observation_list
        temp['sortie'] = str(uuid.uuid4())
        temp['version'] = self.version

        return json.dumps(temp)

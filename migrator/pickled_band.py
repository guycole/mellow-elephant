#
# Title:sortie.py
# Description: pickle container
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

class PickledBand:

    def __init__(self, name, note, sortie_uuid, installation_uuid):
        self.installation_uuid = installation_uuid
        self.name = name
        self.note = note
        self.sortie_uuid = sortie_uuid
        self.observations = []

    def add_observation(self, frequency, sample, time_stamp):
        observation = (frequency, sample, time_stamp)
        self.observations.append(observation)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***

#
# Title:discovery.py
# Description:
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os

class Discovery:

    def discoverSorties(self, dataDirectory):
        """
        only directories w/a sortie file are eligible for upload
        """
        result = []

        directories = os.listdir(dataDirectory)
        for directory in directories:
            target = dataDirectory + "/" + directory + "/sortie.p"
            if os.path.isfile(target):
                result.append(target)

        return result

    def discoverObservations(self, sortieFile):
        """
        :param sortie:
        :return:
        """
        result = []

        ndx = sortieFile.rfind('/')
        tweaked = sortieFile[:ndx]

        targets = os.listdir(tweaked)
        for target in targets:
            if target.startswith('observation'):
                fileName = tweaked + "/" + target
                result.append(fileName)

        return result

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

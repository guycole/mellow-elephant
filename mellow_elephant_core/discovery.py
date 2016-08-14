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
        only directories w/a sortie.p file are ready for upload
        """
        result = []

        directories = os.listdir(dataDirectory)
        for directory in directories:
            target = "%s/%s" % (dataDirectory, directory)

            test = "%s/%s/sortie.p" % (dataDirectory, directory)
            if (os.path.isfile(test)):
                result.append(target)

        return result

    def discoverObservations(self, sortieDirectory):
        """
        return a list of observation files
        """
        result = []

        targets = os.listdir(sortieDirectory)
        for target in targets:
            target = "%s/%s" % (sortieDirectory, target)
            result.append(target)

        return result

    def discoverObservationName(self, fileName):
        """
        given a observation file name return base file name
        """
        ndx = 1 + fileName.rfind('/')
        return fileName[ndx:]

    def discoverSortieName(self, directory):
        """
        given a directory name return sortie id
        """
        ndx = 1 + directory.rfind('/')
        return directory[ndx:]

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***

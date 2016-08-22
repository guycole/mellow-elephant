#! /usr/bin/python
#
# Title:processing.py
# Description: mellow elephant processing/reporting
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import datetime
import pickle
import os
import sys
import yaml

from band_bc780 import BandBc780Factory

from boto.s3.connection import S3Connection
from boto.s3.key import Key

class Processing:

    def process_graph(self, pickled_band):
        raw_file_name = "%s.dat" % pickled_band.get_filename('/tmp')
        output = open(raw_file_name, 'w')
        for observation in pickled_band.observations:
            output.write("%f %d\n" % (observation.frequency/10000.0, observation.sample))
        output.close()

        band_factory = BandBc780Factory()
        frequency_band = band_factory.factory(pickled_band.band_ndx)

        full_name = "%s.png" % pickled_band.get_filename(plot_directory)
        buffer1 = "set output '%s'\n" % full_name
        buffer2 = "set title '%f to %f (band %d)'\n" % (frequency_band.frequency_low, frequency_band.frequency_high, pickled_band.band_ndx)
        buffer3 = "plot '%s'\n" % raw_file_name

        temp_file_name = '/tmp/plot.dem'
        output = open(temp_file_name, 'w')
        output.write("set terminal png small\n")
        output.write("set timestamp\n")
        output.write("set grid\n")
        output.write("set style data line\n")
        output.write(buffer1)
        output.write(buffer2)
        output.write(buffer3)
        output.close()

        command = "%s %s" % (plot_command, temp_file_name)
        os.system(command)

        os.unlink(raw_file_name)
        os.unlink(temp_file_name)

    def s3upload(self, full_name):
        ndx1 = full_name.rindex('/')
        file_name = full_name[1+ndx1:]

        s3directory = "elephant/elephant-%d-%2.2d" % (datetime.datetime.today().year, datetime.datetime.today().month)
        print s3directory

        s3connection = S3Connection()
        s3bucket = s3connection.get_bucket(s3bucket_name)

        s3key = Key(s3bucket)
        s3key.key = "%s/%s" % (s3directory, file_name)
        s3key.set_contents_from_filename(full_name)
j
    def process_band(self, full_name, pickled_band):
        print pickled_band.band_ndx
        self.process_graph(pickled_band)
        self.s3upload(full_name)

    def execute(self):
        candidates = os.listdir(pickle_directory)
        for candidate in candidates:
            full_name = "%s/%s" % (pickle_directory, candidate)
            with open(full_name, 'rb') as handle:
                pickled_band = pickle.load(handle)
                self.process_band(full_name, pickled_band)
                os.unlink(full_name)

print 'start'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        fileName = "config.yaml"

    configuration = yaml.load(file(fileName))

    pickle_directory = configuration['pickleDirectory']
    plot_directory = configuration['plotDirectory']
    pickle_directory = configuration['pickleDirectory']

    plot_command = configuration['gnuplotCommand']

    s3bucket_name = configuration['s3bucket']

    driver = Processing()
    driver.execute()

print 'stop'
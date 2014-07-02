#
# Title:BandBc780.py
# Description:BC-780 frequency band
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
class BandBc780:
	def __init__(self, bandNdx, frequencyLow, frequencyHigh, frequencyStep, modulation):
		self.bandNdx = bandNdx
		self.frequencyLow = frequencyLow
		self.frequencyHigh = frequencyHigh
		self.frequencyStep = frequencyStep
		self.modulation = modulation

class BandBc780Factory:
	def factory(self, bandNdx):
		if bandNdx == 1:
			return BandBc780(bandNdx, 25.0000, 26.9600, 5.0, 'AM')
		elif bandNdx == 2:
			return BandBc780(bandNdx, 26.9650, 27.4050, 5.0, 'AM')
		elif bandNdx == 3:
			return BandBc780(bandNdx, 27.4100, 27.9950, 5.0, 'AM')
		elif bandNdx == 4:
			return BandBc780(bandNdx, 28.0000, 29.6900, 10.0, 'FM')
		elif bandNdx == 5:
			return BandBc780(bandNdx, 29.7000, 49.9900, 10.0, 'FM')
		elif bandNdx == 6:
			return BandBc780(bandNdx, 50.0000, 53.9900, 10.0, 'FM')
		elif bandNdx == 7:
			return BandBc780(bandNdx, 54.0000, 71.9500, 50.0, 'WFM')
		elif bandNdx == 8:
			return BandBc780(bandNdx, 72.0000, 75.9950, 5.0, 'FM')
		elif bandNdx == 9:
			return BandBc780(bandNdx, 76.0000, 87.9500, 50.0, 'WFM')
		elif bandNdx == 10:
			return BandBc780(bandNdx, 88.0000, 107.9000, 100.0, 'WFM')
		elif bandNdx == 11:
			return BandBc780(bandNdx, 108.0000, 136.9750, 25.0, 'AM')
		elif bandNdx == 12:
			return BandBc780(bandNdx, 137.0000, 143.9950, 5.0, 'FM')
		elif bandNdx == 13:
			return BandBc780(bandNdx, 144.0000, 147.9950, 5.0, 'FM')
		elif bandNdx == 14:
			return BandBc780(bandNdx, 148.0000, 161.9950, 5.0, 'FM')
		elif bandNdx == 15:
			return BandBc780(bandNdx, 162.0000, 173.9875, 12.5, 'FM')
		elif bandNdx == 16:
			return BandBc780(bandNdx, 174.0000, 215.9500, 50.0, 'WFM')
		elif bandNdx == 17:
			return BandBc780(bandNdx, 216.0000, 224.9950, 5.0, 'FM')
		elif bandNdx == 18:
			return BandBc780(bandNdx, 225.0000, 399.9500, 50.0, 'AM')
		elif bandNdx == 19:
			return BandBc780(bandNdx, 400.0000, 405.9875, 12.5, 'NFM')
		elif bandNdx == 20:
			return BandBc780(bandNdx, 406.0000, 419.9875, 12.5, 'NFM')
		elif bandNdx == 21:
			return BandBc780(bandNdx, 420.0000, 424.9875, 12.5, 'NFM')
		elif bandNdx == 22:
			return BandBc780(bandNdx, 425.0000, 429.9875, 12.5, 'NFM')
		elif bandNdx == 23:
			return BandBc780(bandNdx, 430.0000, 449.9875, 12.5, 'NFM')
		elif bandNdx == 24:
			return BandBc780(bandNdx, 450.0000, 454.9875, 12.5, 'NFM')
		elif bandNdx == 25:
			return BandBc780(bandNdx, 455.0000, 459.9875, 12.5, 'NFM')
		elif bandNdx == 26:
			return BandBc780(bandNdx, 460.0000, 464.9875, 12.5, 'NFM')
		elif bandNdx == 27:
			return BandBc780(bandNdx, 465.0000, 469.9875, 12.5, 'NFM')
		elif bandNdx == 28:
			return BandBc780(bandNdx, 470.0000, 472.9875, 12.5, 'NFM')
		elif bandNdx == 29:
			return BandBc780(bandNdx, 473.0000, 475.9875, 12.5, 'NFM')
		elif bandNdx == 30:
			return BandBc780(bandNdx, 476.0000, 478.9875, 12.5, 'NFM')
		elif bandNdx == 31:
			return BandBc780(bandNdx, 479.0000, 481.9875, 12.5, 'NFM')
		elif bandNdx == 32:
			return BandBc780(bandNdx, 482.0000, 484.9875, 12.5, 'NFM')
		elif bandNdx == 33:
			return BandBc780(bandNdx, 485.0000, 487.9875, 12.5, 'NFM')
		elif bandNdx == 34:
			return BandBc780(bandNdx, 488.0000, 490.9875, 12.5, 'NFM')
		elif bandNdx == 35:
			return BandBc780(bandNdx, 491.0000, 493.9875, 12.5, 'NFM')
		elif bandNdx == 36:
			return BandBc780(bandNdx, 494.0000, 496.9875, 12.5, 'NFM')
		elif bandNdx == 37:
			return BandBc780(bandNdx, 497.0000, 499.9875, 12.5, 'NFM')
		elif bandNdx == 38:
			return BandBc780(bandNdx, 500.0000, 502.9875, 12.5, 'NFM')
		elif bandNdx == 39:
			return BandBc780(bandNdx, 503.0000, 505.9875, 12.5, 'NFM')
		elif bandNdx == 40:
			return BandBc780(bandNdx, 506.0000, 508.9875, 12.5, 'NFM')
		elif bandNdx == 41:
			return BandBc780(bandNdx, 509.0000, 511.9875, 12.5, 'NFM')
		elif bandNdx == 42:
			return BandBc780(bandNdx, 806.0000, 823.9875, 12.5, 'NFM')
		elif bandNdx == 43:
			return BandBc780(bandNdx, 849.0125, 850.9875, 12.5, 'NFM')
		elif bandNdx == 44:
			return BandBc780(bandNdx, 851.0000, 868.9875, 12.5, 'NFM')
		elif bandNdx == 45:
			return BandBc780(bandNdx, 894.0125, 895.9875, 12.5, 'NFM')
		elif bandNdx == 46:
			return BandBc780(bandNdx, 896.0000, 901.0000, 12.5, 'NFM')
		elif bandNdx == 47:
			return BandBc780(bandNdx, 901.0125, 934.9875, 12.5, 'NFM')
		elif bandNdx == 48:
			return BandBc780(bandNdx, 935.0000, 940.0000, 12.5, 'NFM')
		elif bandNdx == 49:
			return BandBc780(bandNdx, 940.0125, 956.0000, 12.5, 'NFM')
		elif bandNdx == 50:
			return BandBc780(bandNdx, 1240.0000, 1300.0000, 12.5, 'NFM')
		else:
			print "unsupported bandNdx:%d" % bandNdx
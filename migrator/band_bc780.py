#
# Title:band_bc780.py
# Description:BC-780 frequency band
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
class BandBc780:
    def __init__(self, band_ndx, band_name, frequency_low, frequency_high, frequency_step, modulation):
        self.band_ndx = band_ndx
        self.band_name = band_name
        self.frequency_low = frequency_low
        self.frequency_high = frequency_high
        self.frequency_step = frequency_step
        self.modulation = modulation

    def __str__(self):
        return "%d:%f:%f:%f:%s" % (self.band_ndx, self.frequency_low, self.frequency_high, self.frequency_step, self.modulation)

class BandBc780Factory:
    def matcher(self, frequency):
        tweaked_frequency = frequency/10000

        bandNdx = 1
        while band_ndx < 51:
            band = self.factory(band_ndx)
            if tweaked_frequency > band.frequency_high:
                band_ndx += 1
            else:
                return band_ndx;

    def factory(self, band_ndx):
        if band_ndx == 1:
            return BandBc780(band_ndx, 'b1a', 25.0000, 26.9600, 5.0, 'AM')
        elif band_ndx == 2:
            return BandBc780(band_ndx, 'b2a', 26.9650, 27.4050, 5.0, 'AM')
        elif band_ndx == 3:
            return BandBc780(band_ndx, 'b3a', 27.4100, 27.9950, 5.0, 'AM')
        elif band_ndx == 4:
            return BandBc780(band_ndx, 'b4a', 28.0000, 29.6900, 10.0, 'FM')
        elif band_ndx == 5:
            return BandBc780(band_ndx, 'b5a', 29.7000, 49.9900, 10.0, 'FM')
        elif band_ndx == 6:
            return BandBc780(band_ndx, 'b6a', 50.0000, 53.9900, 10.0, 'FM')
        elif band_ndx == 7:
            return BandBc780(band_ndx, 'b7a', 54.0000, 71.9500, 50.0, 'WFM')
        elif band_ndx == 8:
            return BandBc780(band_ndx, 'b8a', 72.0000, 75.9950, 5.0, 'FM')
        elif band_ndx == 9:
            return BandBc780(band_ndx, 'b9a', 76.0000, 87.9500, 50.0, 'WFM')
        elif band_ndx == 10:
            return BandBc780(band_ndx, 'b10a', 88.0000, 107.9000, 100.0, 'WFM')
        elif band_ndx == 11:
            return BandBc780(band_ndx, 'b11a', 108.0000, 136.9750, 25.0, 'AM')
        elif band_ndx == 12:
            return BandBc780(band_ndx, 'b12a', 137.0000, 143.9950, 5.0, 'FM')
        elif band_ndx == 13:
            return BandBc780(band_ndx, 'b13a', 144.0000, 147.9950, 5.0, 'FM')
        elif band_ndx == 14:
            return BandBc780(band_ndx, 'b14a', 148.0000, 161.9950, 5.0, 'FM')
        elif band_ndx == 15:
            return BandBc780(band_ndx, 'b14b', 162.0000, 173.9875, 12.5, 'FM')
        elif band_ndx == 16:
            return BandBc780(band_ndx, 'b15a', 174.0000, 215.9500, 50.0, 'WFM')
        elif band_ndx == 17:
            return BandBc780(band_ndx, 'b16a', 216.0000, 224.9950, 5.0, 'FM')
        elif band_ndx == 18:
            return BandBc780(band_ndx, 'b17a', 225.0000, 399.9500, 50.0, 'AM')
        elif band_ndx == 19:
            return BandBc780(band_ndx, 'b18a', 400.0000, 405.9875, 12.5, 'NFM')
        elif band_ndx == 20:
            return BandBc780(band_ndx, 'b19a', 406.0000, 419.9875, 12.5, 'NFM')
        elif band_ndx == 21:
            return BandBc780(band_ndx, 'b20a', 420.0000, 424.9875, 12.5, 'NFM')
        elif band_ndx == 22:
            return BandBc780(band_ndx, 'b20b', 425.0000, 429.9875, 12.5, 'NFM')
        elif band_ndx == 23:
            return BandBc780(band_ndx, 'b20c', 430.0000, 449.9875, 12.5, 'NFM')
        elif band_ndx == 24:
            return BandBc780(band_ndx, 'b21a', 450.0000, 454.9875, 12.5, 'NFM')
        elif band_ndx == 25:
            return BandBc780(band_ndx, 'b21b', 455.0000, 459.9875, 12.5, 'NFM')
        elif band_ndx == 26:
            return BandBc780(band_ndx, 'b21c', 460.0000, 464.9875, 12.5, 'NFM')
        elif band_ndx == 27:
            return BandBc780(band_ndx, 'b21d', 465.0000, 469.9875, 12.5, 'NFM')
        elif band_ndx == 28:
            return BandBc780(band_ndx, 'b22a', 470.0000, 472.9875, 12.5, 'NFM')
        elif band_ndx == 29:
            return BandBc780(band_ndx, 'b22b', 473.0000, 475.9875, 12.5, 'NFM')
        elif band_ndx == 30:
            return BandBc780(band_ndx, 'b22c', 476.0000, 478.9875, 12.5, 'NFM')
        elif band_ndx == 31:
            return BandBc780(band_ndx, 'b22d', 479.0000, 481.9875, 12.5, 'NFM')
        elif band_ndx == 32:
            return BandBc780(band_ndx, 'b22e', 482.0000, 484.9875, 12.5, 'NFM')
        elif band_ndx == 33:
            return BandBc780(band_ndx, 'b22f', 485.0000, 487.9875, 12.5, 'NFM')
        elif band_ndx == 34:
            return BandBc780(band_ndx, 'b22g', 488.0000, 490.9875, 12.5, 'NFM')
        elif band_ndx == 35:
            return BandBc780(band_ndx, 'b22h', 491.0000, 493.9875, 12.5, 'NFM')
        elif band_ndx == 36:
            return BandBc780(band_ndx, 'b22i', 494.0000, 496.9875, 12.5, 'NFM')
        elif band_ndx == 37:
            return BandBc780(band_ndx, 'b22j', 497.0000, 499.9875, 12.5, 'NFM')
        elif band_ndx == 38:
            return BandBc780(band_ndx, 'b22k', 500.0000, 502.9875, 12.5, 'NFM')
        elif band_ndx == 39:
            return BandBc780(band_ndx, 'b22i', 503.0000, 505.9875, 12.5, 'NFM')
        elif band_ndx == 40:
            return BandBc780(band_ndx, 'b22m', 506.0000, 508.9875, 12.5, 'NFM')
        elif band_ndx == 41:
            return BandBc780(band_ndx, 'b22n', 509.0000, 511.9875, 12.5, 'NFM')
        elif band_ndx == 42:
            return BandBc780(band_ndx, 'b23a', 806.0000, 823.9875, 12.5, 'NFM')
        elif band_ndx == 43:
            return BandBc780(band_ndx, 'b23b', 849.0125, 850.9875, 12.5, 'NFM')
        elif band_ndx == 44:
            return BandBc780(band_ndx, 'b23c', 851.0000, 868.9875, 12.5, 'NFM')
        elif band_ndx == 45:
            return BandBc780(band_ndx, 'b23d', 894.0125, 895.9875, 12.5, 'NFM')
        elif band_ndx == 46:
            return BandBc780(band_ndx, 'b23e', 896.0000, 901.0000, 12.5, 'NFM')
        elif band_ndx == 47:
            return BandBc780(band_ndx, 'b23f', 901.0125, 934.9875, 12.5, 'NFM')
        elif band_ndx == 48:
            return BandBc780(band_ndx, 'b23g', 935.0000, 940.0000, 12.5, 'NFM')
        elif band_ndx == 49:
            return BandBc780(band_ndx, 'b23h', 940.0125, 956.0000, 12.5, 'NFM')
        elif band_ndx == 50:
            return BandBc780(band_ndx, 'b24a', 1240.0000, 1300.0000, 12.5, 'NFM')
        else:
            print "unsupported band_ndx:%d" % band_ndx

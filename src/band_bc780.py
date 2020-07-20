#
# Title:band_bc780.py
# Description:BC-780 frequency band
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
class BandBc780:
    def __init__(
        self, band_ndx, frequency_low, frequency_high, frequency_step, modulation
    ):
        self.band_ndx = band_ndx
        self.frequency_low = frequency_low
        self.frequency_high = frequency_high
        self.frequency_step = frequency_step
        self.modulation = modulation

    def __str__(self):
        return "%d:%f:%f:%f:%s" % (
            self.band_ndx,
            self.frequency_low,
            self.frequency_high,
            self.frequency_step,
            self.modulation,
        )


class BandBc780Factory:
    def matcher(self, frequency):
        tweaked_frequency = frequency / 10000

        band_ndx = 1
        while band_ndx < 51:
            band = self.factory(band_ndx)
            if tweaked_frequency > band.frequency_high:
                band_ndx += 1
            else:
                return band_ndx

    def factory(self, band_ndx):
        if band_ndx == 1:
            return BandBc780(band_ndx, 25.0000, 26.9600, 5.0, "AM")
        elif band_ndx == 2:
            return BandBc780(band_ndx, 26.9650, 27.4050, 5.0, "AM")
        elif band_ndx == 3:
            return BandBc780(band_ndx, 27.4100, 27.9950, 5.0, "AM")
        elif band_ndx == 4:
            return BandBc780(band_ndx, 28.0000, 29.6900, 10.0, "FM")
        elif band_ndx == 5:
            return BandBc780(band_ndx, 29.7000, 49.9900, 10.0, "FM")
        elif band_ndx == 6:
            return BandBc780(band_ndx, 50.0000, 53.9900, 10.0, "FM")
        elif band_ndx == 7:
            return BandBc780(band_ndx, 54.0000, 71.9500, 50.0, "WFM")
        elif band_ndx == 8:
            return BandBc780(band_ndx, 72.0000, 75.9950, 5.0, "FM")
        elif band_ndx == 9:
            return BandBc780(band_ndx, 76.0000, 87.9500, 50.0, "WFM")
        elif band_ndx == 10:
            return BandBc780(band_ndx, 88.0000, 107.9000, 100.0, "WFM")
        elif band_ndx == 11:
            return BandBc780(band_ndx, 108.0000, 136.9750, 25.0, "AM")
        elif band_ndx == 12:
            return BandBc780(band_ndx, 137.0000, 143.9950, 5.0, "FM")
        elif band_ndx == 13:
            return BandBc780(band_ndx, 144.0000, 147.9950, 5.0, "FM")
        elif band_ndx == 14:
            return BandBc780(band_ndx, 148.0000, 161.9950, 5.0, "FM")
        elif band_ndx == 15:
            return BandBc780(band_ndx, 162.0000, 173.9875, 12.5, "FM")
        elif band_ndx == 16:
            return BandBc780(band_ndx, 174.0000, 215.9500, 50.0, "WFM")
        elif band_ndx == 17:
            return BandBc780(band_ndx, 216.0000, 224.9950, 5.0, "FM")
        elif band_ndx == 18:
            return BandBc780(band_ndx, 225.0000, 399.9500, 50.0, "AM")
        elif band_ndx == 19:
            return BandBc780(band_ndx, 400.0000, 405.9875, 12.5, "NFM")
        elif band_ndx == 20:
            return BandBc780(band_ndx, 406.0000, 419.9875, 12.5, "NFM")
        elif band_ndx == 21:
            return BandBc780(band_ndx, 420.0000, 424.9875, 12.5, "NFM")
        elif band_ndx == 22:
            return BandBc780(band_ndx, 425.0000, 429.9875, 12.5, "NFM")
        elif band_ndx == 23:
            return BandBc780(band_ndx, 430.0000, 449.9875, 12.5, "NFM")
        elif band_ndx == 24:
            return BandBc780(band_ndx, 450.0000, 454.9875, 12.5, "NFM")
        elif band_ndx == 25:
            return BandBc780(band_ndx, 455.0000, 459.9875, 12.5, "NFM")
        elif band_ndx == 26:
            return BandBc780(band_ndx, 460.0000, 464.9875, 12.5, "NFM")
        elif band_ndx == 27:
            return BandBc780(band_ndx, 465.0000, 469.9875, 12.5, "NFM")
        elif band_ndx == 28:
            return BandBc780(band_ndx, 470.0000, 472.9875, 12.5, "NFM")
        elif band_ndx == 29:
            return BandBc780(band_ndx, 473.0000, 475.9875, 12.5, "NFM")
        elif band_ndx == 30:
            return BandBc780(band_ndx, 476.0000, 478.9875, 12.5, "NFM")
        elif band_ndx == 31:
            return BandBc780(band_ndx, 479.0000, 481.9875, 12.5, "NFM")
        elif band_ndx == 32:
            return BandBc780(band_ndx, 482.0000, 484.9875, 12.5, "NFM")
        elif band_ndx == 33:
            return BandBc780(band_ndx, 485.0000, 487.9875, 12.5, "NFM")
        elif band_ndx == 34:
            return BandBc780(band_ndx, 488.0000, 490.9875, 12.5, "NFM")
        elif band_ndx == 35:
            return BandBc780(band_ndx, 491.0000, 493.9875, 12.5, "NFM")
        elif band_ndx == 36:
            return BandBc780(band_ndx, 494.0000, 496.9875, 12.5, "NFM")
        elif band_ndx == 37:
            return BandBc780(band_ndx, 497.0000, 499.9875, 12.5, "NFM")
        elif band_ndx == 38:
            return BandBc780(band_ndx, 500.0000, 502.9875, 12.5, "NFM")
        elif band_ndx == 39:
            return BandBc780(band_ndx, 503.0000, 505.9875, 12.5, "NFM")
        elif band_ndx == 40:
            return BandBc780(band_ndx, 506.0000, 508.9875, 12.5, "NFM")
        elif band_ndx == 41:
            return BandBc780(band_ndx, 509.0000, 511.9875, 12.5, "NFM")
        elif band_ndx == 42:
            return BandBc780(band_ndx, 806.0000, 823.9875, 12.5, "NFM")
        elif band_ndx == 43:
            return BandBc780(band_ndx, 849.0125, 850.9875, 12.5, "NFM")
        elif band_ndx == 44:
            return BandBc780(band_ndx, 851.0000, 868.9875, 12.5, "NFM")
        elif band_ndx == 45:
            return BandBc780(band_ndx, 894.0125, 895.9875, 12.5, "NFM")
        elif band_ndx == 46:
            return BandBc780(band_ndx, 896.0000, 901.0000, 12.5, "NFM")
        elif band_ndx == 47:
            return BandBc780(band_ndx, 901.0125, 934.9875, 12.5, "NFM")
        elif band_ndx == 48:
            return BandBc780(band_ndx, 935.0000, 940.0000, 12.5, "NFM")
        elif band_ndx == 49:
            return BandBc780(band_ndx, 940.0125, 956.0000, 12.5, "NFM")
        elif band_ndx == 50:
            return BandBc780(band_ndx, 1240.0000, 1300.0000, 12.5, "NFM")
        else:
            print("unsupported band_ndx:%d" % band_ndx)

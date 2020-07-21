mellow-elephant introduction
==================

Mellow Elephant is an application which uses old radio scanners such as the [Uniden BC-780-XLT](https://wiki.radioreference.com/index.php/BC780XLT) (or similar) to create a database of spectrum utilization.  The database is created by mechanically stepping through the spectrum and observing signal strength.  Sampling continues for an extended period.  Continuous emitters should be observed on every pass, while transient stations might take awhile to discover.

The image below is a sample graph produced by a mellow-elephant utility.  

//output graph

The BC-780-XLT was one of the earliest radio scanners to allow control by computer, in this case via [RS-232](https://en.wikipedia.org/wiki/RS-232).  Controlling the scanner is similar to the [Hayes command set](https://en.wikipedia.org/wiki/Hayes_command_set) in that one writes a simple ASCII string to the device and then read the results.  There is a subset of the BC-780-XLT command set summarized in a table near the end of this file.

There are many popular variations on the BC-780-XLT such as the Radio Shack PRO-2052 all w/similar behavior.  Examples of the BC-780-XLT are readily available via eBay.  The BC-780-XLT are mediocre receivers, and do suffer from poor intermods (in my case, harmonics from commercial FM broadcasters are a problem).  

The image below depicts my current deployment strategy, I use a [Raspberry Pi 3](https://en.wikipedia.org/wiki/Raspberry_Pi) running mellow-elephant to control a BC-780-XLT via RS-232 and a [USB](https://en.wikipedia.org/wiki/USB) adapter.

// Deployment Graphic
// System Picture

getting started
==================

Ready to put an old radio to work?  Place the mellow-elephant sources on a 
raspberry pi and cable the rpi w/your BC-780-XLT.

Place the BC-780-XLT in "RMT" mode.

Establish RS-232 configuration.

Test (need test application)

configure for collection
==================

Uniden divided coverage into various "bands" which I also use to manage frequencies of interest.  "Bands" don't actually map to service types, but there is some overlap.  I provide a band table at the end of this file.


RS-232 
==================

Configuration: 9600, etc 

Here is a more complete [command summary](http://www.netfiles.ru/share/linked/f1/UnidenProtocol.pdf)

| Command | Arguments | Note                |
| ------- | --------- | ------------------- |
| RF      | 1234568   | Receiver Frequency  |
| RM      | N/A       | Receiver Modulation |
| SG      | N/A       | Signal Strength     |
| SI      | N/A       | System Information  |

uniden bands
==================

| Index | Band # | Lower   | Upper   | Increment | Modulation |
| ----- | ------ | ------- | ------- | --------- | ---------- |
| 1     | 1      | 25.0000 | 26.9600 | 5.0       | AM         |
| 2     | 2      | 26.9650 | 27.4050 | 5.0       | AM         |
| 3     | 3      | 27.4100 | 27.9950 | 5.0       | AM         |
| 4     | 4      | 28.0000 | 29.6900 | 10.0      | FM         |
| 5     | 5      | 29.7000 | 49.9900 | 10.0      | FM         |
| 6     | 6      | 50.0000 | 53.9900 | 10.0      | FM         |
| 7     | 7      | 54.0000 | 71.9500 | 50.0      | WFM        |
| 8     | 8      | 72.0000 | 75.9950 | 5.0       | FM         |
| 9     | 9      | 76.0000 | 87.9500 | 50.0      | WFM        |
| 10    | 10     | 88.0000 | 107.9000 | 100.0    | WFM        |
| 11    | 11     | 108.0000 | 136.9750 | 25.0    | AM         |
| 12    | 12     | 137.0000 | 143.9950 | 5.0     | FM         |
| 13    | 13     | 144.0000 | 147.9950 | 5.0     | FM         |
| 14    | 14     | 148.0000 | 161.9950 | 5.0     | FM         |
| 15    | 15     | 162.0000 | 173.9875 | 12.5    | FM         |


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

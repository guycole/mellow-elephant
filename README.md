introduction
==================

Mellow Elephant is an application which uses old radio scanners such as the [Uniden BC-780-XLT](https://wiki.radioreference.com/index.php/BC780XLT) (or similar) to create a database of spectrum utilization.  The database is created by mechanically stepping through the spectrum and observing signal strength.  Sampling continues for an extended period.  Continuous emitters should be observed on every pass, while transient emitters might take awhile to discover.

Here is a sample graph from Mellow Elephant of my local FM broadcast band. The line w/ticks represents signal strength (and each tick is a sample), and the peak values represent active emitters.  The continuous line represents a moving average signal strength and establishes a signal threshold. ![sample graph](https://github.com/guycole/mellow-elephant/blob/master/dox/grafix/1596503454-10.png)

Here is a process overview of Mellow Elephant ![overview](https://github.com/guycole/mellow-elephant/blob/master/dox/grafix/overview.png).  

I use a [Raspberry Pi 3](https://en.wikipedia.org/wiki/Raspberry_Pi) running mellow-elephant to control a BC-780-XLT via RS-232 and a [USB](https://en.wikipedia.org/wiki/USB) adapter.  Here is a photo of the actual equipment. ![]( https://github.com/guycole/mellow-elephant/blob/master/dox/grafix/elephant_rear.png)


Uniden BC-780-XLT
==================

The BC-780-XLT was one of the earliest radio scanners to allow control by computer, in this case via [RS-232](https://en.wikipedia.org/wiki/RS-232).  Controlling the scanner is similar to the [Hayes command set](https://en.wikipedia.org/wiki/Hayes_command_set) in that one writes a simple ASCII string to the device and then read the results.  There is more about the BC-780-XLT command set near the end of this file.

There are many popular variations on the BC-780-XLT such as the Radio Shack PRO-2052 all w/similar behavior.  Examples of the BC-780-XLT are readily available via eBay.  The BC-780-XLT are mediocre receivers, and do suffer from poor intermods (in my case, harmonics from commercial FM broadcasters are a problem).  

The BC-780-XLT defines chunks of spectrum into bands (table at end of file) which loosely map to spectrum service allocation.  Mellow Elephant can be configured to search or ignore by Uniden band.

getting started
==================

Ready to put an old radio to work?  See the project [documentation](https://github.com/guycole/mellow-elephant/blob/master/dox/open_office/mellow_elephant.pdf)

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

| Index | Band # | Lower     | Upper     | Increment | Modulation |
| ----- | ------ | --------- | --------- | --------- | ---------- |
| 1     | 1      |   25.0000 |   26.9600 |   5.0     | AM         |
| 2     | 2      |   26.9650 |   27.4050 |   5.0     | AM         |
| 3     | 3      |   27.4100 |   27.9950 |   5.0     | AM         |
| 4     | 4      |   28.0000 |   29.6900 |  10.0     | FM         |
| 5     | 5      |   29.7000 |   49.9900 |  10.0     | FM         |
| 6     | 6      |   50.0000 |   53.9900 |  10.0     | FM         |
| 7     | 7      |   54.0000 |   71.9500 |  50.0     | WFM        |
| 8     | 8      |   72.0000 |   75.9950 |   5.0     | FM         |
| 9     | 9      |   76.0000 |   87.9500 |  50.0     | WFM        |
| 10    | 10     |   88.0000 |  107.9000 | 100.0     | WFM        |
| 11    | 11     |  108.0000 |  136.9750 |  25.0     | AM         |
| 12    | 12     |  137.0000 |  143.9950 |   5.0     | FM         |
| 13    | 13     |  144.0000 |  147.9950 |   5.0     | FM         |
| 14    | 14     |  148.0000 |  161.9950 |   5.0     | FM         |
| 15    | 14     |  162.0000 |  173.9875 |  12.5     | FM         |
| 16    | 15     |  174.0000 |  215.9500 |  50.0     | WFM        |
| 17    | 16     |  216.0000 |  224.9950 |   5.0     | FM         |
| 18    | 17     |  225.0000 |  399.9500 |  50.0     | AM         |
| 19    | 18     |  400.0000 |  405.9875 |  12.5     | NFM        |
| 20    | 19     |  406.0000 |  419.9875 |  12.5     | NFM        |
| 21    | 20     |  420.0000 |  424.9875 |  12.5     | NFM        |
| 22    | 20     |  425.0000 |  429.9875 |  12.5     | NFM        |
| 23    | 20     |  430.0000 |  449.9875 |  12.5     | NFM        |
| 24    | 21     |  450.0000 |  454.9875 |  12.5     | NFM        |
| 25    | 21     |  455.0000 |  459.9875 |  12.5     | NFM        |
| 26    | 21     |  460.0000 |  464.9875 |  12.5     | NFM        |
| 27    | 21     |  465.0000 |  469.9875 |  12.5     | NFM        |
| 28    | 22     |  470.0000 |  472.9875 |  12.5     | NFM        |
| 29    | 22     |  473.0000 |  475.9875 |  12.5     | NFM        |
| 30    | 22     |  476.0000 |  478.9875 |  12.5     | NFM        |
| 31    | 22     |  479.0000 |  481.9875 |  12.5     | NFM        |
| 32    | 22     |  482.0000 |  484.9875 |  12.5     | NFM        |
| 33    | 22     |  485.0000 |  487.9875 |  12.5     | NFM        |
| 34    | 22     |  488.0000 |  490.9875 |  12.5     | NFM        |
| 35    | 22     |  491.0000 |  493.9875 |  12.5     | NFM        |
| 36    | 22     |  494.0000 |  496.9875 |  12.5     | NFM        |
| 37    | 22     |  497.0000 |  499.9875 |  12.5     | NFM        |
| 38    | 22     |  500.0000 |  502.9875 |  12.5     | NFM        |
| 39    | 22     |  503.0000 |  505.9875 |  12.5     | NFM        |
| 40    | 22     |  506.0000 |  508.9875 |  12.5     | NFM        |
| 41    | 22     |  509.0000 |  511.9875 |  12.5     | NFM        |
| 42    | 23     |  806.0000 |  823.9875 |  12.5     | NFM        |
| 43    | 23     |  849.0125 |  850.9875 |  12.5     | NFM        |
| 44    | 23     |  851.0000 |  868.9875 |  12.5     | NFM        |
| 45    | 23     |  894.0125 |  895.9875 |  12.5     | NFM        |
| 46    | 23     |  896.0000 |  901.0000 |  12.5     | NFM        |
| 47    | 23     |  901.0125 |  934.9875 |  12.5     | NFM        |
| 48    | 23     |  935.0000 |  940.0000 |  12.5     | NFM        |
| 49    | 23     |  940.0125 |  956.0000 |  12.5     | NFM        |
| 50    | 24     | 1240.0000 | 1300.0000 |  12.5     | NFM        |

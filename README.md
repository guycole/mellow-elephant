mellow-elephant introduction
==================

Mellow Elephant uses old radio scanners such as the [Uniden BC-780-XLT](https://wiki.radioreference.com/index.php/BC780XLT) or similar to create a database of spectrum utilization.  

The BC-780-XLT was one of the earliest radio scanners to allow control by computer, in this case via a RS-232 link.  Controlling the scanner is similar to the [Hayes command set](https://en.wikipedia.org/wiki/Hayes_command_set) in that one writes a simple ASCII string to the device and then read the results.

There are many popular variations on the BC-780-XLT such as the Radio Shack (add me) all w/similar behavior.

For the Mellow Elephant application, I command the scanner to visit a radio frequency and the read the signal strength.  Then onto the next frequency to repeat.  Over time, I will have enough observations to know where there are stations that are continuously emitting, and where some are transient.  If interesting, I can follow up w/more sophisticated receivers and methods.

The BC-780-XLT is old enough to be cheaply available via eBay.  These are fair receivers, although they do suffer from poor intermods (in my case, harmonics from commercial FM broadcasters are a problem).  

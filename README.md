# CWBeacon
Poorly coded first try at a morse code beacon with a graphical front end. This script uses the gerryk https://github.com/gerryk/cwbeacon beacon.py script to fire a relay attached to a GPIO pin to key a transceiver with morse code to send a beacon out. 

 You must get the beacon.py script from https://github.com/gerryk/cwbeacon put it in the same folder as the other scripts and then rename it to txbeacon.py for this script to function. 

The primary script accepts input from the user, and creates a config file, then calls a subprocess (beaconout.py) config file is read by "beaconout.py"  to create a string to call the Gerry K beacon.py (I renamed to txbeacon.py) 

For my use I modified Gerry K's script to use GPIO 26 and renamed it to "txbeacon.py".

I used Tkinter (not really recommended) for the graphics, I used configparser for getting the inputs and writing them to a config file. I used a subprocess to run the actual beacon so I would have a method of killing it. Probably not the best method but it functions sort of. 

There is essentially zero error checking, this means that this is HIGH RISK if connected to a transceiver, as the lack of error checking could lead to an open or locked transmit that could let the smoke out of your transceiver! 

Many thanks to Gerry K for his beacon.py script, it was the motivating force for creating this script! 



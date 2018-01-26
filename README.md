# PSKBeacon
Poorly coded first try at a PSK31lx beacon with a graphical front end to key transceiver with psk31 message to send a beacon out. 
I used Tkinter (not really recommended) for the graphics, I used configparser for getting the inputs and writing them to a config file. I used a subprocess to run the actual beacon so I would have a method of killing it. Probably not the best method but it functions sort of. 

There is essentially zero error checking, this means that this is HIGH RISK if connected to a transceiver, as the lack of error checking could lead to an open or locked transmit that could let the smoke out of your transceiver! 

This software just assembles the beacon text into a file and copies that file every XX minutes. 

A modified version of PSK31lx is required to transmit and receive the PSK31 via vox on a transceiver.

updates to follow.... 


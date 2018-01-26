#!/usr/bin/env python
import os
import time
import six

if six.PY2:
    import ConfigParser as configparser
else:
    import configparser
import sys


parser = configparser.ConfigParser()
parser.read('pskbeacon.conf')

print(parser.get('MessageConfig', 'Callsign1'))
print(parser.get('MessageConfig', 'Callsign2'))
print(parser.get('MessageConfig', 'Message'))
print(parser.getint('MessageConfig', 'timer'))

callsign1Get = (parser.get('MessageConfig', 'Callsign1'))
callsign2Get = (parser.get('MessageConfig', 'Callsign2'))
messageGet = (parser.get('MessageConfig', 'message'))
timerGet = (parser.getint('MessageConfig', 'timer'))

newbeaconVal = " " + callsign2Get + " " + callsign2Get +" DE " + callsign1Get +" "+ callsign1Get +" "+ messageGet
with open('beacontext.txt', 'w+') as f:
    f.write(newbeaconVal)
    f.close
filetransport = "sudo cp beacontext.txt /home/pi/tx/beacontext.txt"


while True:
   os.system(filetransport)
   time.sleep(timerGet)




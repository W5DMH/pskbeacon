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
parser.read('CWBeacon.conf')

print(parser.get('MessageConfig', 'Callsign1'))
print(parser.get('MessageConfig', 'Callsign2'))
print(parser.get('MessageConfig', 'Message'))
print(parser.getint('MessageConfig', 'timer'))

callsign1Get = (parser.get('MessageConfig', 'Callsign1'))
callsign2Get = (parser.get('MessageConfig', 'Callsign2'))
messageGet = (parser.get('MessageConfig', 'message'))
timerGet = (parser.getint('MessageConfig', 'timer'))

newbeaconVal = "./txbeacon.py -c 20 " + callsign2Get + " " + callsign2Get +" DE " + callsign1Get +" "+ callsign1Get +" "+ messageGet
print(newbeaconVal)


while True:
   os.system(newbeaconVal)
   time.sleep(timerGet)




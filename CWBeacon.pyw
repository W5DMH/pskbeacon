#!/usr/bin/env python
# Name this file echo.py
import os
import time
import subprocess
#from configparser import ConfigParser
import six
if six.PY2:
    import ConfigParser as configparser
else:
    import configparser
from Tkinter import*
from subprocess import call
from sys import executable


window = Tk()
#Top = Tk ()


C1in = StringVar()
C2in = StringVar()
messageValue = StringVar()
beacontimerin = StringVar()
C1 = None
C2 = None
messageout = None 
beacontimer = None

window.title("CWBeacon")
window.geometry("600x400+500+250")
window.configure(bg="blue")
label = Label(window,text = "Enter Callsign and message in the boxes below")
label.configure(bg='yellow')
label.place(x= 50, y=25)

Beacon=[]
#From Callsign Entry
label = Label(window, text="Your Callsign")
label.configure(bg='Yellow')
label.place(x=50, y=70)
entry_box1=Entry(window,textvariable=C1in)
entry_box1.place(x=140,y=70, width=75)

# To Callsign Entry
label = Label(window, text="To Callsign")
label.configure(bg='Yellow')
label.place(x=50, y=110)
entry_box2=Entry(window,textvariable=C2in)
entry_box2.place(x=127,y=110, width=75)

# Beacon Timer Entry
label = Label(window, text="Beacon Timer in seconds")
label.configure(bg='Yellow')
label.place(x=210, y=110)
entry_box4=Entry(window,textvariable=beacontimerin)
entry_box4.place(x=380,y=110, width=75)


#Message  Entry
label = Label(window, text="25 char Message")
label.configure(bg='Yellow')
label.place(x=50, y=150)

def limitSizeMessage(*args):
    value = messageValue.get()
    if len(value) > 25: messageValue.set(value[:25])

messageValue = StringVar()
messageValue.trace('w', limitSizeMessage)

entry_box3=Entry(window,textvariable=messageValue)
entry_box3.place(x=168, y=150, width=210)

# Function

def enter():
    global C1in, C2in, messageValue,beacontimer, newbeaconVal  
    C1 = C1in.get()
    C2 = C2in.get()
    messageout = messageValue.get()
    beacontimer = beacontimerin.get()
    #print C1
    #print C2
    #print messageout
    #print beacontimer
    parser = configparser.ConfigParser()

    parser.add_section('MessageConfig') 
    parser.set('MessageConfig', 'Callsign1', C1)
    parser.set('MessageConfig', 'Callsign2', C2)
    parser.set('MessageConfig', 'Message', messageout)
    parser.set('MessageConfig', 'Timer', beacontimer)

    parser.write(sys.stdout)
    with open('CWBeacon.conf', 'w') as configfile:
       parser.write(configfile)

    
proc = None

def turnOn():
    global proc
    if proc is None:
        print('Starting Beacon')
        proc = subprocess.Popen(["python", "/home/pi/PiCW/beaconout.py"])
      

def turnOff():
    global proc
    if proc is not None:
        print('Beacon Stopped')
        proc.terminate()
        proc = None

on = Button(window, borderwidth=2, text = "Start Beacon", width=15, pady=5, command = turnOn)
off = Button(window, borderwidth=2, text = "Stop Beacon", width=15, pady=5, command = turnOff)
on.place(x=215,y=200)
off.place(x=380,y=200)
#on.grid()
#off.grid()


def stop():
    window.destroy()
    #Top.destroy()

b = Button(window, borderwidth=2, text="Save Beacon Settings", width=15, pady=5, command=enter)
b.place(x=50,y=200)
b = Button(window, borderwidth=2, text="Exit", width=12, pady=5, command=stop)
b.place(x=250,y=350)

window.mainloop()


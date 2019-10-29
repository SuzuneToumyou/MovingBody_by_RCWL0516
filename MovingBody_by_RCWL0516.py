#!/usr/bin/python3
#coding: utf-8

from gpiozero import DigitalInputDevice
import datetime
import ambient

from signal import pause

ambi = ambient.Ambient(ID, "writeKey")
radar = DigitalInputDevice(18, pull_up=False, bounce_time=2.0)

def detector():
    timestamp = str((datetime.datetime.now()))
    timestamp = timestamp[0:19]
    print("Image captured at",timestamp)
    
    h=1
    r = ambi.send({"d1": h})
    r.close()
    
radar.when_activated = detector
pause()

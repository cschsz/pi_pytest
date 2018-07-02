#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT) #gruen
GPIO.setup(16, GPIO.OUT) #rot
GPIO.setup(32, GPIO.OUT) #rot
GPIO.setup(36, GPIO.OUT) #gruen

galaxys7 = 1
t_s7 = time.time()
galaxys5 = 1
t_s5 = time.time()

#----------------------------------------[prot]
def prot(name, dauer):
    if dauer  == 0:
        zeile = "%s %s ist nicht erreichbar\r\n" % (time.strftime("%d.%m.%Y %H:%M:%S"), name) 
        f = open("/home/pi/log", "a")
        f.write(zeile)
        f.close()
    else:
        zeile = "%s %s ist wieder erreichbar nach %s Minuten\r\n" % (time.strftime("%d.%m.%Y %H:%M:%S"), name, sekunden / 60) 
        f = open("/home/pi/log", "a")
        f.write(zeile)
        f.close()

#----------------------------------------[ledblink]
def ledblink(ledein, ledaus):
    GPIO.output(ledein, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(ledein, GPIO.HIGH)
    GPIO.output(ledaus, GPIO.LOW)

#----------------------------------------[main]
zeile = "%s Start...\r\n" % (time.strftime("%d.%m.%Y %H:%M:%S")) 
f = open("/home/pi/log", "a")
f.write(zeile)
f.close()

try:
    while 1:

        if os.system("ping -c 1 -w 2 " + "192.168.1.100") == 0:
            ledblink(12, 16)
            if galaxys7 == 0:
                sekunden = time.time() - t_s7
                prot("GalaxyS7", sekunden)
                galaxys7 = 1
            t_s7 = time.time()
        else:
            ledblink(16, 12)
            if galaxys7 == 1:
                galaxys7 = 0
                prot("GalaxyS7", 0)

        if os.system("ping -c 1 -w 2 " + "192.168.1.102") == 0:
            ledblink(36, 32)
            if galaxys5 == 0:
                sekunden = time.time() - t_s5
                prot("GalaxyS5", sekunden)
                galaxys5 = 1
            t_s5 = time.time()
        else:
            ledblink(32, 36)
            if galaxys5 == 1:
                galaxys5 = 0
                prot("GalaxyS5", 0)

        time.sleep(5)

#----------------------------------------[]
except KeyboardInterrupt:
    GPIO.cleanup()

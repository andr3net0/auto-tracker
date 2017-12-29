#!/usr/bin/python
# Copyright (c) 2017 Logicc Systems Ltd.
# Author: Andre Neto
# based on Daniel Bull's LiPoPi project - https://github.com/NeonHorizon/lipopi
  
import RPi.GPIO as GPIO
from time import sleep
import datetime
import pickle
import sys
import os
import logging


try:
    import settings
except  Exception, e:
    print e
    print __name__ + ": Could not perform import"
    sys.exit(1)

try:
    serial          = settings.PI_KEY
    verbose         = settings.VERBOSE
    WARNING         = settings.WARNING
    PWR_ON_OUT      = settings.PWR_ON_OUT
    PWR_LBO_IN      = settings.PWR_LBO_IN
    PWR_OFF_IN      = settings.PWR_OFF_IN
except Exception, e:
    print e
    print "Could not read settings"
    sys.exit(1)

# create logger with 'pwrMngmtIO'
logger = logging.getLogger('pwrMngmtIO')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('logs/pwrMngmtIO.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  


# Define a threaded callback function to run in another thread when events are detected  
def lbo_callback(pin):
    sleep(4)
    global status
    value = 'LOW' if GPIO.input(pin) == 0 else 'OK'
    if value != status:
        status = value
        entry = [('Power-LBO'+'@'+str(serial), value, 'power')]
        if verbose:
            logger.info('Ran lbo_calback. Result: ' + value)
            print entry[0]
            print
        #putDataDB.postData(entry)
        if WARNING:
            logger.info('(Dummy) Setting warning: ' + value)
            #setWarning.setWarn(entry)
            #update_lastStatusRecord(entry[0])

        #os.system("sudo shutdown now")

# when a changing edge is detected on port 'PWR_LBO_IN', regardless of whatever   
# else is happening in the program, the function my_callback will be run
GPIO.setup(PWR_LBO_IN, GPIO.IN)
GPIO.add_event_detect(PWR_LBO_IN, GPIO.BOTH, callback=lbo_callback, bouncetime=1000)  
status = 'OK'


# Define a threaded callback function to run in another thread when events are detected  
def pwr_off_callback(pin):
    sleep(4)
    shutdown = (GPIO.input(pin) == 1)
    entry = [('Power-Off-Button'+'@'+str(serial), 'shutdown' if shutdown else 'keep on', 'power')]
    if verbose:
        logger.info('Ran pwr_off_callback. Result: ' + str(shutdown))
        print entry[0]
        print
    if shutdown:
        #putDataDB.postData(entry)
        if WARNING:
            logger.info('(Dummy) Setting warning: ' + 'shutting down!')
            #setWarning.setWarn(entry)
            #update_lastStatusRecord(entry[0])
        cmd = "sudo wall 'System shutting down in %d seconds'" % 10
        os.system(cmd)
        sleep(10)
        os.system("sudo shutdown now")

# when a changing edge is detected on port 'PWR_OFF_IN', regardless of whatever   
# else is happening in the program, the function my_callback will be run
GPIO.setup(PWR_OFF_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(PWR_OFF_IN, GPIO.BOTH, callback=pwr_off_callback, bouncetime=1000)


# main loop
try:
    logger.info('Starting up')
    while 1:
        sleep(300)
        if WARNING:
            logger.info('Still active')
        

except Exception,e:
    print e
    print "Interrupted"
    logger.info('Interrupted')
    logger.error(e)
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  

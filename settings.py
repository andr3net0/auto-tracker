# settings for getTemps.py

# getTemps script switches
APIPOST = True # change to enable/disable api posting
VERBOSE = True # change to enable/disable verbose output
WARNING = True # change to enable/disable Siren/Beacon output

# API Settings
URL = 'your api endpoint url'
URL_LIMTS = 'your api endpoint url - get temperature limits'
URL_WARN = 'your api endpoint url - send warning email'
API_KEY = 'your api key'
PI_KEY = 'your pi serial'

# DHT Info
DHT_V = 11      # DHT version '11': Adafruit_DHT.DHT11, '22': Adafruit_DHT.DHT22, '2302': Adafruit_DHT.AM2302 
DHT_PINS = [17, 27]

# PINs used for power controll
PWR_ON_OUT = 25 # internal pull down
PWR_LBO_IN =  8 # internal pull up
PWR_OFF_IN = 24


# Door sensors 
DOOR_PINS = [22]
OPEN_VALUE = 1
MAX_OPEN_TIME = 2*60 # max time door open - seconds

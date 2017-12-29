# settings for getTemps.py

# getTemps script switches
APIPOST = True # change to enable/disable api posting
VERBOSE = True # change to enable/disable verbose output
WARNING = True # change to enable/disable Siren/Beacon output

# TIMING Settings
SAMPLING_PERIOD = 2     # time betwen samples  (minutes) minimum: 1, max 59
APIPOST_PERIOD  = 10    # time betwen api post (minutes) minimum: 1, max 59

# API Settings
URL = 'your api endpoint url'
URL_LIMTS = 'your api endpoint url - get temperature limits'
URL_WARN = 'your api endpoint url - send warning email'
API_KEY = 'your api key'
PI_KEY = 'your pi serial'

# DB Settings
DB_NAME = "database.db" # DB name for measures and params
SQL_FILE_NAME = "db_init.sql" # sql name to DB init

# DHT Info
DHT_V = 11      # DHT version '11': Adafruit_DHT.DHT11, '22': Adafruit_DHT.DHT22, '2302': Adafruit_DHT.AM2302 
DHT_PINS = [17,27]

# CT / ADC Info
ADC_CHANNELS = [0,1]

# Software SPI configuration - MCP3008 ADC:
CLK  = 6
MISO = 13
MOSI = 19
CS   = 26

# Door sensors 
DOOR_PINS = [22]
OPEN_VALUE = 1
MAX_OPEN_TIME = 2*60 # max time door open - seconds

# Siren/Beacon
WARN_PIN = 21
SIGNAL_TIME = 5
MAX_TIME_SOUND = 5 * 60         # max time sound plays - seconds
TEMPERATURE_WARN_DELAY = 10 * 60     # delay to start temperature alert
TEMPERATURE_VALID_MIN = -10      # sets the minimum value to valid measures
TEMPERATURE_VALID_MAX = 50     # sets the maximum value to valid measures

TEMP_ABOVE_AUDIO_FILE = 'above.mp3'
TEMP_BELOW_AUDIO_FILE = 'below.mp3'
DOOR_OPEN_AUDIO_FILE = 'door.mp3'

# Clear warning pin
CLEAR_WARN_PIN = 5
BUTTON_MIN_INTERVAL = 15 * 60   # min time from last button call - seconds
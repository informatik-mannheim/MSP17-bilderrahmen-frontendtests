from testValues import *

# WEBAPP System

# Adress of the webapp
WEBAPP_URL="" 

# Google Test Accounts
# First user should have a few picture already uploaded
WEBAPP_VALUE_USER_1_MAIL=''
WEBAPP_VALUE_USER_1_PWD=''

# This user will always clean the drive pictures on tear down
WEBAPP_VALUE_USER_2_MAIL=''
WEBAPP_VALUE_USER_2_PWD=''

# Only used for one testcase. Dont use this account on ionic app
WEBAPP_NO_IONIC_USE_VALUE_USER_MAIL=''
WEBAPP_NO_IONIC_USE_VALUE_USER_PWD=''



# IONIC APP System and devices
IONIC_APP_SETTINGS_AUTO_START="false"
IONIC_APP_SETTINGS_SERVER_ADRESSE=""

# Capabilities for both devices (Android)
PACKAGE='de.hsmannheim.bilderrahmen'
ACTIVITY='.MainActivity'
NO_RESET=True
FULL_RESET=False
CLEAR_SYSTEM_FILES=False
PLATFORM_NAME="Android"
APP_PATH_CONFIG=PATH("")
NEW_COMMAND_TIMEOUT='5000'

# important! use ports minimu 2 numbers away! One instanz of appium uses more ports https://github.com/appium/appium/issues/3592
# adb problems: https://github.com/appium/appium/issues/5949
#https://github.com/appium/appium/issues/6665

# ANDROID DEVICE 1
APPIUM_PORT1="4723" #this is the default port from appium
device1_desired_caps = {}
device1_desired_caps['udid']=''
device1_desired_caps['platformName'] = PLATFORM_NAME
device1_desired_caps['platformVersion'] =""
device1_desired_caps['deviceName'] = ''
#device1_desired_caps['app'] = APP_PATH_CONFIG   
device1_desired_caps['appPackage'] = PACKAGE 
device1_desired_caps['appActivity'] = ACTIVITY
device1_desired_caps['noReset']=NO_RESET
device1_desired_caps['newCommandTimeout'] = NEW_COMMAND_TIMEOUT
#device1_desired_caps['fullReset']=FULL_RESET
#device1_desired_caps['clearSystemFiles']=CLEAR_SYSTEM_FILES
device1_desired_caps['autoWebview']=True

# ANDROID DEVICE 2
APPIUM_PORT2="65500"
device2_desired_caps = {}
device2_desired_caps['platformName'] = PLATFORM_NAME
device2_desired_caps['udid']=''
device2_desired_caps['newCommandTimeout'] = NEW_COMMAND_TIMEOUT
device2_desired_caps['platformVersion'] = ""
device2_desired_caps['deviceName'] = '' 
#device2_desired_caps['app'] = APP_PATH_CONFIG   
device2_desired_caps['appPackage'] = PACKAGE 
device2_desired_caps['appActivity'] = ACTIVITY
device2_desired_caps['noReset']=NO_RESET
#device2_desired_caps['fullReset']=FULL_RESET
#device2_desired_caps['clearSystemFiles']=CLEAR_SYSTEM_FILES
#device2_desired_caps['autoWebview']=True


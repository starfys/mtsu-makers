#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import Adafruit_DHT
import time
import requests

import csv
#ID of the raspberry pi
pi_id = 1

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to pin 23.
pin = 11
while True:
	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	# Note that sometimes you won't get a reading and
	# the results will be null (because Linux can't
	# guarantee the timing of calls to read the sensor).  
	# If this happens try again!
	if humidity is not None and temperature is not None:
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	else:
		print 'Failed to get reading. Try again!'
        time.sleep(300)
        try:
                requests.post( "http://stevensheffey.me:9000/tempHumidity/submit", data={ 'pi_num':pi_id, 'temperature':temperature, 'humidity': humidity, 'date_rec':time.time() } )
        except:
                print "failed to connect to server"
                #the expected filename should be Tue.Aug.11.pinum1.txt
                #should take time like once a week to check on sd cards, so this doesn't do it ad infinitum, 
                filename=".".join(time.ctime().split(' ')[0:3])+".pinum"+str(pi_id)+".txt"
                with open(filename,'a') as csvfile:
                        fieldnames=['pi_num', 'temperature','humidity', 'date_rec']
                        writer= csv.Dictwriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({ 'pi_num':pi_id, 'temperature':temperature, 'humidity': humidity, 'date_rec':time.time()) })

import Adafruit_BBIO.GPIO as GPIO
from hcsr04sensor import sensor

# This script uses a static method inside the Measurement class
# called basic_distance
# No median readings pulled from a sample for error correction
# No setmode in the library
# No pin cleanups.  You handle all of these things in your own code
# Just a simple return of a cm distance as reported directly from Rpi.GPIO
# Only returns a metric value.

# set gpio pins
trig = "P9_23"
echo = "P9_25"

GPIO.setwarnings(False)
x = sensor.Measurement
# use default temp of 20 Celcius
distance_warm = x.basic_distance(trig, echo)

# example of passing temperature reading
# temperature affects speed of sound
# Easily combine with a temperature sensor to pass the current temp
temp = -30
distance_cold = x.basic_distance(trig, echo, celsius=temp)

print("The distance at  20 Celsius is {} cm's".format(distance_warm))
print("The distance at -30 Celsius is {} cm's".format(distance_cold))
# cleanup gpio pins.
GPIO.cleanup((trig, echo))

import Adafruit_BBIO.GPIO as GPIO
from hcsr04sensor import sensor

# Created by Al Audet
# MIT License


def main():
    """Calculate the distance of an object in centimeters using a HCSR04 sensor
       and a Raspberry Pi"""
    # Use GPIO.BOARD values instead of BCM
    trig_pin = "P9_23"
    echo_pin = "P9_25"
    # Default values
    # unit = 'metric'
    # temperature = 20

    # Create a distance reading with the hcsr04 sensor module
    # using GPIO.BOARD pin values.
    value = sensor.Measurement(trig_pin, echo_pin)
    raw_measurement = value.raw_distance()

    # Calculate the distance in centimeters
    print("The Distance = {} centimeters".format(round(raw_measurement, 1)))


if __name__ == "__main__":
    main()

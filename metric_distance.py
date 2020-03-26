from sensor import Measurement

# Created by Al Audet
# MIT License


def main():
    """Calculate the distance of an object in centimeters using a HCSR04 sensor
       and a Raspberry Pi"""

    trig_pin = "P9_23"
    echo_pin = "P9_25"
    
    # Default values
    # unit = 'metric'
    # temperature = 20 (room temp in Celsius)

    #  Create a distance reading with the hcsr04 sensor module
    value = Measurement(trig_pin, echo_pin)
    raw_measurement = value.raw_distance()

    # To overide default room temp you can pass the following to value
    # This can be combined with a temperature sensor for cold weather apps.
    # value = sensor.Measurement(trig_pin,
    #                            echo_pin,
    #                            temperature=2,
    #                            )

    # Calculate the distance in centimeters
    print("The Distance = {} centimeters".format(round(raw_measurement, 6)))


if __name__ == "__main__":
    main()

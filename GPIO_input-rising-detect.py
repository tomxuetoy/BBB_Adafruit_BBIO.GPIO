import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)
GPIO.cleanup()

GPIO.setup("P8_14", GPIO.IN)
GPIO.wait_for_edge("P8_14", GPIO.RISING)
print("rising edge comes")

# connect P8_14 and P8_10 pins on BBB

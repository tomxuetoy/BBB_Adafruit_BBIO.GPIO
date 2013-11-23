import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)
GPIO.cleanup()

GPIO.setup("P8_14", GPIO.IN)
if GPIO.input("P8_14"):
    print("HIGH")
else:
    print("LOW")

# connect P8_14 and P8_10 pins on BBB

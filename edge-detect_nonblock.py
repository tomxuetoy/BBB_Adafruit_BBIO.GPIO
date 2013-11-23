import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)
GPIO.cleanup()

GPIO.setup("P8_14", GPIO.IN)
GPIO.add_event_detect("P8_14", GPIO.RISING)

#your amazing code here
print "let us sleep for 5 seconds..."
time.sleep(5)

#detect wherever:
if GPIO.event_detected("P8_14"):
    print "event detected!"

# connect P8_14 and P8_10 pins on BBB

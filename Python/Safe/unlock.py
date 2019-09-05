import RPi.GPIO as GPIO
import time

signalPin = 2
positionVal = 2

try:
    if float(positionVal) > 0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(signalPin, GPIO.OUT)
        servo = GPIO.PWM(signalPin, 50)

        try:
            servo.start(7.5)

            servo.ChangeDutyCycle(float(positionVal))
            time.sleep(0.5)

            servo.stop()
        except Exception as ei:
            servo.stop()
            print(ei)
except Exception as eo:
    print(eo)
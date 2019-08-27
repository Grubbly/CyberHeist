import RPi.GPIO as GPIO
import time

signalPin = 14

def moveServo(positionVal):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signalPin, GPIO.OUT)

    servo = GPIO.PWM(signalPin, 50)
    servo.start(7.5)

    servo.ChangeDutyCycle(float(positionVal))
    time.sleep(0.5)

    servo.stop()
    GPIO.cleanup()
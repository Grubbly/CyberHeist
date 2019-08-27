import RPi.GPIO as GPIO
import time

signalPin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(signalPin, GPIO.OUT)

servo = GPIO.PWM(signalPin, 50)
servo.start(7.5)

servo.ChangeDutyCycle(7.5)
time.sleep(0.3)
servo.ChangeDutyCycle(10)
time.sleep(0.3)
servo.ChangeDutyCycle(7.5)
time.sleep(0.3)
servo.ChangeDutyCycle(10)
time.sleep(0.3)

servo.stop()
GPIO.cleanup()
#!/bin/python

import RPi.GPIO as GPIO
import time

led_vermelho=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_vermelho, GPIO.OUT)

while True:
	GPIO.output(led_vermelho, GPIO.HIGH)
	print("LED ACESO")
	time.sleep(1)
	print("LED APAGADO")
	GPIO.output(led_vermelho, GPIO.LOW)
	time.sleep(1)





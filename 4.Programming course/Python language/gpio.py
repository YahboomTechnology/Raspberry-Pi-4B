#/usr/bin/env python3
#coding=utf-8

import wiringpi

GPIO_Pin = 0
OUTPUT = 1
HIGH = 1
LOW = 0

wiringpi.wiringPiSetup()
wiringpi.pinMode(GPIO_Pin,OUTPUT)

while 1:
    print ('Set GPIO_Pin => H')
    wiringpi.digitalWrite(GPIO_Pin,HIGH)
    wiringpi.delay(500)
    print ('Set GPIO_Pin => L')
    wiringpi.digitalWrite(GPIO_Pin,LOW)
    wiringpi.delay(500)
#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as gpio
import time

class led_flash:
    #initialize
    def __init__(self, green_led_pin, blue_led_pin):
        self.green_led_pin=green_led_pin
        self.blue_led_pin=blue_led_pin
        # gpio setup
        gpio.setmode(gpio.BCM) # Broadcom Mode, Index of Pin
        gpio.setup(self.green_led_pin, gpio.OUT)
        gpio.setup(self.blue_led_pin, gpio.OUT)
        
        gpio.output(self.green_led_pin,False)
        gpio.output(self.blue_led_pin,False)
        
    def toggle(self, led_pin, interval):
        # print(led_pin)
        while True:
            if led_pin=="GREEN":
                gpio.output(self.green_led_pin,True)
                time.sleep(interval)
                gpio.output(self.green_led_pin,False)
                time.sleep(interval)
            elif led_pin=="BLUE":
                gpio.output(self.blue_led_pin,True)
                time.sleep(interval)
                gpio.output(self.blue_led_pin,False)
                time.sleep(interval)

if __name__ == '__main__':
    print("LED MODULE SELF TESTING")
    gpio.cleanup()
    led=led_flash(17,27)
    led.toggle("GREEN", 1)

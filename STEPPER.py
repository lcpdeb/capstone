#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as gpio
import time

class stepper:
    def __init__(self, step_pin, dir_pin, ms1_pin, ms2_pin, ms3_pin, enable_pin, mode, step_time=0.001):
        self.step = step_pin
        self.dir = dir_pin
        self.ms1=ms1_pin
        self.ms2=ms2_pin
        self.ms3=ms3_pin
        self.enable=enable_pin
        self.mode=mode

        # gpio setup
        gpio.setmode(gpio.BCM) # Broadcom Mode, Index of Pin
        gpio.setup(self.step, gpio.OUT)
        gpio.setup(self.dir, gpio.OUT)
        gpio.setup(self.ms1, gpio.OUT)
        gpio.setup(self.ms2, gpio.OUT)
        gpio.setup(self.ms3, gpio.OUT)
        gpio.setup(self.enable, gpio.OUT)
        
        # initial
        gpio.output(self.step, False)
        gpio.output(self.dir, False)
        gpio.output(self.ms1, False)
        gpio.output(self.ms2, False)
        gpio.output(self.ms3, False)
        gpio.output(self.enable, False)
        

        self.step_time = step_time 
        self.steps_per_rev = 1600
        self.current_position = 0
       

    def steps(self, step_count=1):
        print("Moving Forward")
        #当step_count为正数的时候，设置dir引脚为低电平。否则为高电平。
        if step_count > 0:
            print("Moving Forward")
            gpio.output(self.dir, False)
        else:
            print("Moving Backward")
            gpio.output(self.dir, True)

        for i in range(abs(step_count)):
            gpio.output(self.step, True)
            time.sleep(self.step_time)
            gpio.output(self.step, False)
            time.sleep(self.step_time)
        self.current_position += step_count

    # def relative_angle(self, angle):

    # def absolute_angle(self, angle):

if __name__ == '__main__':
    print("STEPPER MODULE SELF TESTING")
    step_pin=26
    dir_pin=19
    enable_pin=13
    stepper=stepper(step_pin,dir_pin,6,5,12,enable_pin,0)
    stepper.steps()
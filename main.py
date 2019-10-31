#!/usr/bin/env python
# encoding: utf-8
import time, RPi.GPIO, threading
from LED import led_flash
from STEPPER import stepper
# pin statement
green_led_pin=17
blue_led_pin=27

step_pin=26
dir_pin=19
ms1_pin=6
ms2_pin=5
ms3_pin=21
enable_pin=13
# initialize
led=led_flash(green_led_pin,blue_led_pin)
stepper=stepper(step_pin,dir_pin,ms1_pin,ms2_pin,ms3_pin,enable_pin,0)

threads=[]
task1=threading.Thread(target=led.toggle,args=("GREEN",1/4))
threads.append(task1)
task2=threading.Thread(target=led.toggle,args=("BLUE",1/3))
threads.append(task2)
task3=threading.Thread(target=stepper.steps ,args=(1))
threads.append(task3)
if __name__ == '__main__':
    print("RUNNING...")
    try:
        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()
    except KeyboardInterrupt:
        RPi.GPIO.cleanup()

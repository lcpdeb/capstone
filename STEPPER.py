#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO as gpio
import time
from PID import pid
from GYROSCOPE import Gyro

class stepper:
    def __init__(self, FRONT_LEFT, FRONT_RIGHT, BACK_LEFT, BACK_RIGHT,
                 ms1_pin, ms2_pin, ms3_pin, enable_pin, mode, gyro, step_time=0.005, ):
        self.front_left_step_pin = FRONT_LEFT[0]
        self.front_left_dir_pin = FRONT_LEFT[1]
        self.front_right_step_pin = FRONT_RIGHT[0]
        self.front_right_dir_pin = FRONT_RIGHT[1]
        #self.back_left_step_pin = BACK_LEFT[0]
        #self.back_left_dir_pin = BACK_LEFT[1]
        #self.back_right_step_pin = BACK_RIGHT[0]
        #self.back_right_dir_pin = BACK_RIGHT[1]
        self.ms1=ms1_pin
        self.ms2=ms2_pin
        self.ms3=ms3_pin
        self.enable=enable_pin
        self.mode=mode
        self.gyro=gyro

        # gpio setup
        gpio.setmode(gpio.BCM) # Broadcom Mode, Index of Pin
        gpio.setup(self.front_left_step_pin, gpio.OUT)
        gpio.setup(self.front_left_dir_pin, gpio.OUT)
        gpio.setup(self.front_right_step_pin, gpio.OUT)
        gpio.setup(self.front_right_dir_pin, gpio.OUT)
        #gpio.setup(self.back_left_step_pin, gpio.OUT)
        #gpio.setup(self.back_left_dir_pin, gpio.OUT)
        #gpio.setup(self.back_right_step_pin, gpio.OUT)
        #gpio.setup(self.back_right_dir_pin, gpio.OUT)
        gpio.setup(self.ms1, gpio.OUT)
        gpio.setup(self.ms2, gpio.OUT)
        gpio.setup(self.ms3, gpio.OUT)
        gpio.setup(self.enable, gpio.OUT)
        
        # initial
        gpio.output(self.front_left_step_pin, False)
        gpio.output(self.front_left_dir_pin, False)
        gpio.output(self.front_right_step_pin, False)
        gpio.output(self.front_right_dir_pin, False)
        #gpio.output(self.back_left_step_pin, False)
        #gpio.output(self.back_left_dir_pin, False)
        #gpio.output(self.back_right_step_pin, False)
        #gpio.output(self.back_right_dir_pin, False)
        gpio.output(self.ms1, False)
        gpio.output(self.ms2, False)
        gpio.output(self.ms3, False)
        gpio.output(self.enable, False)
        

        self.step_time = step_time 
        self.steps_per_rev = 1600
        self.current_position = 0
       

    # def steps(self, step_count=1):
    #     print("Moving Forward")
    #     #当step_count为正数的时候，设置dir引脚为低电平。否则为高电平。
    #     if step_count > 0:
    #         print("Moving Forward")
    #         gpio.output(self.dir, False)
    #     else:
    #         print("Moving Backward")
    #         gpio.output(self.dir, True)

    #     for i in range(abs(step_count)):
    #         gpio.output(self.step, True)
    #         time.sleep(self.step_time)
    #         gpio.output(self.step, False)
    #         time.sleep(self.step_time)
    #     self.current_position += step_count

    def move_F(self, step_count=265):#260
#        print("FFFFFFFFFFFFF")
        # DIRECTION
        # right side motor
        gpio.output(self.front_right_dir_pin, False)
        #gpio.output(self.back_right_dir_pin, True)
        # left side motor
        gpio.output(self.front_left_dir_pin, True)
        #gpio.output(self.back_left_dir_pin, False)

        # STEP
        for i in range(abs(step_count)):
            gpio.output(self.front_left_step_pin, True)
            gpio.output(self.front_right_step_pin, True)
            #gpio.output(self.back_left_step_pin, True)
            #gpio.output(self.back_right_step_pin, True)
            time.sleep(self.step_time)
            
            gpio.output(self.front_left_step_pin, False)
            if i % 32 ==0:
                continue
            gpio.output(self.front_right_step_pin, False)
            #gpio.output(self.back_left_step_pin, False)
            #gpio.output(self.back_right_step_pin, False)
            time.sleep(self.step_time)
            
    def move_L(self, step_count=132):
#        print("LLLLLLLLLLLLLL")
        # DIRECTION
        # right side motor
        gpio.output(self.front_right_dir_pin, True)
        #gpio.output(self.back_right_dir_pin, True)
        # left side motor
        gpio.output(self.front_left_dir_pin, True)
        #gpio.output(self.back_left_dir_pin, True)

        # STEP
        for i in range(abs(step_count)):
            gpio.output(self.front_left_step_pin, True)
            gpio.output(self.front_right_step_pin, True)
            #gpio.output(self.back_left_step_pin, True)
            #gpio.output(self.back_right_step_pin, True)
            time.sleep(self.step_time)
            gpio.output(self.front_left_step_pin, False)
            gpio.output(self.front_right_step_pin, False)
            #gpio.output(self.back_left_step_pin, False)
            #gpio.output(self.back_right_step_pin, False)
            time.sleep(self.step_time)

    def move_R(self, step_count=120):
#        print("RRRRRRRRRRRRR")
        # DIRECTION
        # right side motor
        gpio.output(self.front_right_dir_pin, False)
        #gpio.output(self.back_right_dir_pin, True)
        # left side motor
        gpio.output(self.front_left_dir_pin, False)
        #gpio.output(self.back_left_dir_pin, True)

        # STEP
        for i in range(abs(step_count)):
            gpio.output(self.front_left_step_pin, True)
            gpio.output(self.front_right_step_pin, True)
            #gpio.output(self.back_left_step_pin, True)
            #gpio.output(self.back_right_step_pin, True)
            time.sleep(self.step_time)
            gpio.output(self.front_left_step_pin, False)
            gpio.output(self.front_right_step_pin, False)
            #gpio.output(self.back_left_step_pin, False)
            #gpio.output(self.back_right_step_pin, False)
            time.sleep(self.step_time)
    
    def move_U(self, step_count=259):
#        print("UUUUUUUUU")
        # DIRECTION
        # right side motor
        gpio.output(self.front_right_dir_pin, False)
        #gpio.output(self.back_right_dir_pin, True)
        # left side motor
        gpio.output(self.front_left_dir_pin, False)
        #gpio.output(self.back_left_dir_pin, True)

        # STEP
        for i in range(abs(step_count)):
            gpio.output(self.front_left_step_pin, True)
            gpio.output(self.front_right_step_pin, True)
            #gpio.output(self.back_left_step_pin, True)
            #gpio.output(self.back_right_step_pin, True)
            time.sleep(self.step_time)
            gpio.output(self.front_left_step_pin, False)
            gpio.output(self.front_right_step_pin, False)
            #gpio.output(self.back_left_step_pin, False)
            #gpio.output(self.back_right_step_pin, False)
            time.sleep(self.step_time)
    # def relative_angle(self, angle):

    # def absolute_angle(self, angle):
    def rotate(self, angle_change):
        
        yaw_pid=pid(p=1, i=1, d=0.00,i_max=50, output_max=90)
        current_roll, current_pitch, current_yaw=self.gyro.get_angle()                                  
        target_yaw=current_yaw+angle_change
#        yaw_error=target_yaw-current_yaw
#        if yaw_error>=180:
#            yaw_error-=360
#        elif yaw_error<=-180:
#            yaw_error+=360
        yaw_error=angle_change
        while abs(yaw_error)>4.5:
            current_roll, current_pitch, current_yaw=self.gyro.get_angle()      
            yaw_error=target_yaw-current_yaw
            if yaw_error>=180:
                yaw_error-=360
            elif yaw_error<=-180:
                yaw_error+=360
#            yaw_output_angle+=yaw_pid.calculate_pid(yaw_error)
#            print('Current:{:4}, Error:{:4}'.format(current_yaw,yaw_error))
            time.sleep(0.01)
#
            if yaw_error > 0:# left
                gpio.output(self.front_left_dir_pin, True)
                gpio.output(self.front_right_dir_pin, True)
            else:# right
                gpio.output(self.front_left_dir_pin, False)
                gpio.output(self.front_right_dir_pin, False)
            
            gpio.output(self.front_left_step_pin, True)
            gpio.output(self.front_right_step_pin, True)
            time.sleep(0.0015)
            gpio.output(self.front_left_step_pin, False)
            gpio.output(self.front_right_step_pin, False)
            time.sleep(0.0015)

            
        
        

if __name__ == '__main__':
    print("STEPPER MODULE SELF TESTING")
#    gpio.cleanup()
    ms1_pin=14
    ms2_pin=14
    ms3_pin=14
    enable_pin=14
    front_left_step_pin=26
    front_left_dir_pin=19

#    back_left_step_pin=6
#    back_left_dir_pin=13
    
    front_right_step_pin=17
    front_right_dir_pin=27

#    back_right_step_pin=17
#    back_right_dir_pin=27
    
    FRONT_LEFT=[front_left_step_pin, front_left_dir_pin]
    FRONT_RIGHT=[front_right_step_pin, front_right_dir_pin]
    BACK_LEFT=[]
    BAKC_RIGHT=[]
    gyro=Gyro(0x50)
    stepper=stepper(FRONT_LEFT,FRONT_RIGHT,BACK_LEFT,BAKC_RIGHT,ms1_pin,ms2_pin,ms3_pin,enable_pin,0,gyro)
    # right side backward
    # stepper.steps(100)
    # left side front
#    stepper.move_L()
#    time.sleep(0.75)
#    stepper.move_F()
#    stepper.rotate(90)
    time.sleep(0.75)
    stepper.move_F()
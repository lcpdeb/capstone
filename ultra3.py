#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering

class UltraSonic_dev:
    FLOOR_BOOL = False                                  #Associate pin 24 to ECHO
    FRONT_BOOL = False                                  #Associate pin 24 to ECHO
    RIGHT1_BOOL = False 
    RIGHT2_BOOL = False 
    BACK_BOOL = False 
    LEFT2_BOOL = False 
    LEFT1_BOOL = False 
    
    
    # Initialize
    def __init__(self, TRIG, ultrasonic_echo_set):
        # setup
        self.TRIG=TRIG
        self.ultrasonic_echo_set=ultrasonic_echo_set
        self.distance=[99999,99999]
        GPIO.setup(self.TRIG,GPIO.OUT)                  #Set pin as GPIO out
        for echo_pin in self.ultrasonic_echo_set:
            GPIO.setup(echo_pin,GPIO.IN)                   #Set pin as GPIO in

    def detecting_process(self, side_set):
        pulse_start=[0,0]
        pulse_end=[0,0]
        pulse_duration=[0,0]
        
        i=0
        for echo_pin in side_set:
            # Trig the ultrasonic soundwave
            GPIO.output(self.TRIG, False)                 #Set TRIG as LOW
            time.sleep(0.01)                            #Delay of 2 seconds
            GPIO.output(self.TRIG, True)                  #Set TRIG as HIGH
            time.sleep(0.00001)                      #Delay of 0.00001 seconds
            GPIO.output(self.TRIG, False)                 #Set TRIG as LOW
            
            while GPIO.input(echo_pin)==0:               #Check whether the ECHO is LOW
                pulse_start[i] = time.time()              #Saves the last known time of LOW pulse
            while GPIO.input(echo_pin)==1:               #Check whether the ECHO is HIGH
                pulse_end[i] = time.time()                #Saves the last known time of HIGH pulse 

            pulse_duration[i] = pulse_end[i] - pulse_start[i] #Get pulse duration to a variable

            self.distance[i] = pulse_duration[i] * 17150        #Multiply pulse duration by 17150 to get distance
            self.distance[i] = round(self.distance[i], 2)            #Round to two decimal points
            i=i+1

#        print('First:{:g}, Second:{:g}'.format(self.distance[0],self.distance[1]))
        time.sleep(0.005)

    def detect(self, direction=None):
        if direction=='left':
#            print("Left Ultrasonic is detecting")
            left_ultrasonic_set=self.ultrasonic_echo_set[4:5+1]
#            while True:
#                self.detecting_process(left_ultrasonic_set)
            k=0
            avg_distance=[]
            while k<10:
                self.detecting_process(left_ultrasonic_set)
                avg_distance.append(self.distance[0])
                k=k+1
            return sum(avg_distance)/10.0
        if direction=='right':
#            print("Right Ultrasonic is detecting")
            right_ultrasonic_set=self.ultrasonic_echo_set[2:3+1]
#            while True:
#                self.detecting_process(right_ultrasonic_set)
            k=0
            avg_distance=[]
            while k<10:
                self.detecting_process(right_ultrasonic_set)
                avg_distance.append(self.distance[0])
                k=k+1
            return sum(avg_distance)/10.0
        if direction=='front':
#            print("Front Ultrasonic is detecting")
            front_ultrasonic_set=self.ultrasonic_echo_set[1:1+1]
#            while True:
#                self.detecting_process(front_ultrasonic_set)
            k=0
            avg_distance=[]
            while k<10:
                self.detecting_process(front_ultrasonic_set)
                avg_distance.append(self.distance[0])
                k=k+1
            return sum(avg_distance)/10.0
        if direction=='back':
#            print("Back Ultrasonic is detecting")
            back_ultrasonic_set=self.ultrasonic_echo_set[6:6+1]
#            while True:
#                self.detecting_process(back_ultrasonic_set)
            k=0
            avg_distance=[]
            while k<10:
                self.detecting_process(back_ultrasonic_set)
                avg_distance.append(self.distance[0])
                k=k+1
            return sum(avg_distance)/10.0

if __name__=='__main__':
    print("Unit Test: Ultrasonic")
#     GPIO.cleanup()
    TRIG = 21                           
    # 20 16 12 7 8 23 24
    FLOOR = 20                              
    FRONT = 23                          
    RIGHT1 = 12
    RIGHT2 = 8
    LEFT1 = 7
    LEFT2 = 16
    BACK = 24
    ultrasonic_echo_set=[FLOOR, FRONT, RIGHT1, RIGHT2, LEFT1, LEFT2, BACK]
    ultrasonic=UltraSonic_dev(TRIG,ultrasonic_echo_set)
    back_flag=ultrasonic.detect(direction='back')
    left_flag=ultrasonic.detect(direction='left')
    right_flag=ultrasonic.detect(direction='right')
    front_flag=ultrasonic.detect(direction='front')
    print(front_flag, left_flag, right_flag, back_flag)


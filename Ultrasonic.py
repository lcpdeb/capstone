#!/usr/bin/env python
# encoding: utf-8
from numpy import *
import time
from isObstacle import isObstacle
from ultra3 import *

def Ultrasonic(path_map):
    left_flag=0
    right_flag=0
    up_flag=0
    down_flag=0



    TRIG = 23                                  #Associate pin 23 to TRIG
    
    FLOOR = 24                                  #Associate pin 24 to ECHO
    FRONT = 25                                 #Associate pin 24 to ECHO
    RIGHT1 = 8
    RIGHT2 = 7
    LEFT1 = 20
    LEFT2 = 16
    BACK = 12
    ultrasonic_echo_set=[FLOOR, FRONT, RIGHT1, RIGHT2, LEFT1, LEFT2, BACK]
    ultrasonic=UltraSonic_dev(TRIG,ultrasonic_echo_set)
    

    # # waiting for ultrasonic sensors
    # left_flag=ultrasonic.detect(direction='left')
    # right_flag=ultrasonic.detect(direction='right')
    # up_flag=ultrasonic.detect(direction='front')
    # down_flag=ultrasonic.detect(direction='back')


    # simulation
    left_position=mat([[path_map.current_position[0,0]-1,path_map.current_position[0,1]]])
    right_position=mat([[path_map.current_position[0,0]+1,path_map.current_position[0,1]]])
    up_position=mat([[path_map.current_position[0,0],path_map.current_position[0,1]+1]])
    down_position=mat([[path_map.current_position[0,0],path_map.current_position[0,1]-1]])
    if isObstacle(left_position,path_map.obstacle):
        left_flag=1
    if isObstacle(right_position,path_map.obstacle):
        right_flag=1
    if isObstacle(up_position,path_map.obstacle):
        up_flag=1
    if isObstacle(down_position,path_map.obstacle):
        down_flag=1


    return left_flag, right_flag, up_flag, down_flag

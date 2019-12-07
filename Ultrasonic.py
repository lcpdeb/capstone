#!/usr/bin/env python
# encoding: utf-8
from numpy import *
import time
from isObstacle import isObstacle
from ultra3 import *

def Ultrasonic(path_map):
    left_flag=0
    right_flag=0
    front_flag=0
    back_flag=0

    DISTANCE_THRESHOLD=35

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
    

    # waiting for ultrasonic sensors
    left_distance=ultrasonic.detect(direction='left')
    right_distance=ultrasonic.detect(direction='right')
    front_distance=ultrasonic.detect(direction='front')
    back_distance=ultrasonic.detect(direction='back')

    if left_distance<=DISTANCE_THRESHOLD:
        left_flag=1
    if right_distance<=DISTANCE_THRESHOLD:
        right_flag=1
    if front_distance<=DISTANCE_THRESHOLD:
        front_flag=1
    if back_distance<=DISTANCE_THRESHOLD:
        back_flag=1
        



#    # simulation
#    left_position=mat([[path_map.current_position[0,0]-1,path_map.current_position[0,1]]])
#    right_position=mat([[path_map.current_position[0,0]+1,path_map.current_position[0,1]]])
#    up_position=mat([[path_map.current_position[0,0],path_map.current_position[0,1]+1]])
#    down_position=mat([[path_map.current_position[0,0],path_map.current_position[0,1]-1]])
#    if isObstacle(left_position,path_map.obstacle):
#        left_flag=1
#    if isObstacle(right_position,path_map.obstacle):
#        right_flag=1
#    if isObstacle(up_position,path_map.obstacle):
#        up_flag=1
#    if isObstacle(down_position,path_map.obstacle):
#        down_flag=1


    return left_flag, right_flag, front_flag, back_flag

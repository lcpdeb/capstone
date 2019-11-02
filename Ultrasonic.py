#!/usr/bin/env python
# encoding: utf-8
from numpy import *
import time
from isObstacle import isObstacle

def Ultrasonic(path_map):
    left_flag=0
    right_flag=0
    up_flag=0
    down_flag=0

    # # waiting for ultrasonic sensors
    # left_flag=ultrasonic_detect(direction='left')
    # right_flag=ultrasonic_detect(direction='right')
    # up_flag=ultrasonic_detect(direction='up')
    # down_flag=ultrasonic_detect(direction='down')


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

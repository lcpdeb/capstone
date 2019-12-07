#!/usr/bin/env python
# encoding: utf-8
from numpy import *
from STEPPER import stepper
import RPi.GPIO as gpio
import time

def Move(last_direction_vector,current_position,next_position, robot_stepper):
    move_direction=""
    # # if last_direction_vector is no exist yet (first step), default UP
    # try:
    #     last_direction_vector
    # except NameError:
    #     last_direction_vector = mat([[0,1]])
    # else:
    #     pass

    # print("last direction,", last_direction_vector)

    if current_position[0,0]<next_position[0,0] and current_position[0,1]==next_position[0,1]:
        
        direction_str="RIGHT"
        # direction vector
        direction_vector=mat([[1,0]])
        trasnmit_matrix=mat([[0,0,0,1],
                             [0,0,1,0],
                             [1,0,0,0],
                             [0,1,0,0]])
    elif current_position[0,0]>next_position[0,0] and current_position[0,1]==next_position[0,1]:
        direction_str="LEFT"
        # direction vector
        direction_vector=mat([[-1,0]])
        trasnmit_matrix=mat([[0,0,1,0],
                             [0,0,0,1],
                             [0,1,0,0],
                             [1,0,0,0]])
    elif current_position[0,0]==next_position[0,0] and current_position[0,1]<next_position[0,1]:
        direction_str="UP"
        # direction vector
        direction_vector=mat([[0,1]])
        trasnmit_matrix=mat([[1,0,0,0],
                             [0,1,0,0],
                             [0,0,1,0],
                             [0,0,0,1]])
    elif current_position[0,0]==next_position[0,0] and current_position[0,1]>next_position[0,1]:
        direction_str="DOWN"
        # direction_vector vector
        direction_vector=mat([[0,-1]])
        trasnmit_matrix=mat([[0,1,0,0],
                             [1,0,0,0],
                             [0,0,0,1],
                             [0,0,1,0]])
    

    # print("now direction", direction_vector)
  
#    # Initialize stepper not really needed
#    ms1_pin=14
#    ms2_pin=14
#    ms3_pin=14
#    enable_pin=14
#    front_left_step_pin=26
#    front_left_dir_pin=19
#
#    back_left_step_pin=6
#    back_left_dir_pin=13
#    
#    front_right_step_pin=2
#    front_right_dir_pin=3
#
#    back_right_step_pin=17
#    back_right_dir_pin=27
#    
#    FRONT_LEFT=[front_left_step_pin, front_left_dir_pin]
#    FRONT_RIGHT=[front_right_step_pin, front_right_dir_pin]
#    BACK_LEFT=[back_left_step_pin, back_left_dir_pin]
#    BAKC_RIGHT=[back_right_step_pin, back_right_dir_pin]
#    
#    robot_stepper=stepper(FRONT_LEFT,FRONT_RIGHT,BACK_LEFT,BAKC_RIGHT,ms1_pin,ms2_pin,ms3_pin,enable_pin,0)
    

    # calculate relative angle by dot product
    cos_theta=(last_direction_vector-mat([[0.02,0.01]]))*(direction_vector+mat([[0.01,0.02]])).transpose()

    if cos_theta == -1.0304 or cos_theta == -0.9703999999999999:
        move_direction="U-turn"
        transmit_vector=mat([[0,-1]])
#        robot_stepper.move_U()
        robot_stepper.rotate(180)
        time.sleep(0.75)
        robot_stepper.move_F()
    elif cos_theta == 1.0096 or cos_theta == 0.9896:
        move_direction="Forward"
        transmit_vector=mat([[0,1]])
        robot_stepper.move_F()
    elif cos_theta == -0.0204 or cos_theta == -0.0003999999999999976 or cos_theta == 0.0196:
        move_direction="Rightward"
        transmit_vector=mat([[1,0]])
        robot_stepper.rotate(-90)
        time.sleep(0.75)
        robot_stepper.move_F()
    elif cos_theta == -0.00040000000000000105 or cos_theta == 0.0396 or cos_theta == -0.0404:
        move_direction="Leftward"
        transmit_vector=mat([[-1,0]])
        robot_stepper.rotate(90)
        time.sleep(0.75)
        robot_stepper.move_F()


    last_direction_vector=direction_vector
    print("MOVE "+move_direction)
    return current_position, trasnmit_matrix, last_direction_vector
    
if __name__ == "__main__":
    print("Unit Test: Move")
    current_grid=mat([[12,12]])
    next_grid=mat([[12,11]])
    last_dir=mat([[0,-1]])
    Move(last_dir,current_grid,next_grid)
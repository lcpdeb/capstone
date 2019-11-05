#!/usr/bin/env python
# encoding: utf-8
from numpy import *

def Move(last_direction_vector,current_position,next_position):
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


    

    # calculate relative angle by dot product
    cos_theta=(last_direction_vector-mat([[0.02,0.01]]))*(direction_vector+mat([[0.01,0.02]])).transpose()

    if cos_theta == -1.0304 or cos_theta == -0.9703999999999999:
        move_direction="U-turn"

        transmit_vector=mat([[0,-1]])
        # Stepper.move_U()
    elif cos_theta == 1.0096 or cos_theta == 0.9896:
        move_direction="Forward"
        transmit_vector=mat([[0,1]])
        # Stepper.move_F()
    elif cos_theta == -0.0204 or cos_theta == -0.0003999999999999976 or cos_theta == 0.0196:
        move_direction="Rightward"
        transmit_vector=mat([[1,0]])
        # Stepper.move_R()
    elif cos_theta == -0.00040000000000000105 or cos_theta == 0.0396 or cos_theta == -0.0404:
        move_direction="Leftward"
        transmit_vector=mat([[-1,0]])
        # Stepper.move_L()


    last_direction_vector=direction_vector
    print("MOVE "+move_direction)
    return current_position, trasnmit_matrix, last_direction_vector
    
if __name__ == "__main__":
    current_grid=mat([[12,12]])
    next_grid=mat([[12,11]])
    last_dir=mat([[1,0]])
    Move(last_dir,current_grid,next_grid)
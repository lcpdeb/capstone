#!/usr/bin/env python
# encoding: utf-8

def Move(current_position,next_position):
    if current_position[0,0]<next_position[0,0] and current_position[0,1]==next_position[0,1]:
        print("MOVE RIGHT.")
        return current_position
    elif current_position[0,0]>next_position[0,0] and current_position[0,1]==next_position[0,1]:
        print("MOVE LEFT.")
        return current_position
    elif current_position[0,0]==next_position[0,0] and current_position[0,1]<next_position[0,1]:
        print("MOVE UP.")
        return current_position
    elif current_position[0,0]==next_position[0,0] and current_position[0,1]>next_position[0,1]:
        print("MOVE DOWN.")
        return current_position
    
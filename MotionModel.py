#!/usr/bin/env python
# encoding: utf-8
from numpy import *

def MotionModel():
    D=1             # x   y   cost
    next_move=mat([ [ 1,  0,  D*1],     # Move right
                    [ 0,  1,  D*1],     # Move up
                    [-1,  0,  D*1],     # Move left
                    [ 0, -1,  D*1]])    # Move down
                    # [ 1,  1,  D*1.414], # Move up-right
                    # [-1, -1,  D*1.414], # Move down-left
                    # [-1,  1,  D*1.414], # Move up-left
                    # [ 1, -1,  D*1.414]])# Move down-right
    return next_move
    
if __name__ == '__main__':
    print("Unit Test - MotionModel: ", print(MotionModel()))
#!/usr/bin/env python
# encoding: utf-8
from numpy import *

def GetBoundary(map_size):
    boundary=mat([[0,0]])
    for i1 in range(1,map_size+2):
        boundary=vstack((boundary,[0,i1]))
    for i2 in range(1,map_size+2):
        boundary=vstack((boundary,[i2,0]))
    for i3 in range(1,map_size+2):
        boundary=vstack((boundary,[map_size+1,i3]))
    for i4 in range(1,map_size+1):
        boundary=vstack((boundary,[i4,map_size+1]))
    return boundary

if __name__ == '__main__':
    print("Unit Test - GetBoundary: \n", GetBoundary(5))
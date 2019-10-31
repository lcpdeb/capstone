#!/usr/bin/env python
# encoding: utf-8
from numpy import *
from isSamePosition import isSamePosition

def isObstacle(m,obstacle):
    for index in range(0,len(obstacle[:,0])):
        if isSamePosition(obstacle[index,:],m[0:2]):
            flag=True
            return flag
    flag=False
    return flag

if __name__ == '__main__':
    obstacle=mat([[0,0],
                  [1,1],
                  [2,2],
                  [3,3],
                  [4,4],
                  [5,5],
                  [6,6]])
    e=mat([[6,6]])
    print("Unit Test - isObstacle: ", isObstacle(e,obstacle))
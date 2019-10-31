#!/usr/bin/env python
# encoding: utf-8
from numpy import *
from isSamePosition import isSamePosition

def FindList(m,open_list,close_list):
    if len(open_list):
        for index in range(0, len(open_list[:,0])):
            if isSamePosition(open_list[index,:],m[0:2]):
                flag=1
                return flag
    if len(close_list):
        for index in range(0, len(close_list[:,0])):
            if isSamePosition(close_list[index,:],m[0:2]):
                flag=2
                return flag
    flag=3
    return flag

if __name__ == '__main__':
    M=mat([[5,6,3,1,2]])
    OPEN_LIST=mat([[1,2,6],
                [6,6,6],
                [7,6,6],
                [7,6,6],
                [8,6,6]])
    CLOSE_LIST=mat([[3,4,6],
                [6,6,6],
                [7,6,6],
                [7,6,6],
                [5,6,6]])
    print("Unit Test - FindList: ", FindList(M,OPEN_LIST,CLOSE_LIST))
#!/usr/bin/env python
# encoding: utf-8
from numpy import *
import time
from isSamePosition import isSamePosition

def GetPath(close_list,start):
    path=mat([[0,0]]) # Create an empty path, zero will be removed after OPTIMAL PATH found
    index=0
    while True:
        path=vstack((path,close_list[index,0:2]))
        if isSamePosition(close_list[index,0:2],start):
            break

        for i in range(0,len(close_list[:,0])):
            if isSamePosition(close_list[i,0:2],close_list[index,3:5]):
                index=i
                break
    # remove first all-zero row from OPTIMAL PATH
    path=delete(path,0,axis=0)
    return path


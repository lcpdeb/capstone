#!/usr/bin/env python
# encoding: utf-8
from numpy import *

def isSamePosition(a,b):
    result=False
    if a[0,0]==b[0,0] and a[0,1]==b[0,1]:
        result=True
    return result

if __name__ == '__main__':
    c=mat([[1,2]])
    d=mat([[1,2]])
    print("Unit Test - isSamePosition: ", isSamePosition(c,d))
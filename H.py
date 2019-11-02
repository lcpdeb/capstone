#!/usr/bin/env python
# encoding: utf-8
from numpy import *

def H(a,b):
    D=1
    # # Manhattan Distance
    # return D*(abs(a[0,0]-b[0,0])+abs(a[0,1]-b[0,1]))
    
    # Eculidean Distance
    return D*(abs(a[0,0]-b[0,0])**2+abs(a[0,1]-b[0,1])**2)

if __name__ == '__main__':
    a=mat([[3,4,5]])
    b=mat([[4,5,6]])
    print("Unit Test - H cost: ", H(a,b))
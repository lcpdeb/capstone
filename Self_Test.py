#!/usr/bin/env python
# encoding: utf-8
from numpy import *
import time
from H import H
from isSamePosition import isSamePosition
from MotionModel import MotionModel
from FindList import FindList
from GetBoundary import GetBoundary
from GetObstacle import GetObstacle
from isObstacle import isObstacle
from Astar import Astar

a=mat([[3,4,5]])
b=mat([[4,5,6]])
print("Self Test - H cost:", H(a,b))
c=mat([[1,2]])
d=mat([[1,2]])
print("Self Test - isSamePosition:", isSamePosition(c,d))
print("Self Test - MotionModel:\n", MotionModel())
M=mat([[9,6,3,1,2]])
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
# print(isSamePosition(OPEN_LIST[0,:],M[0,0:2]))
print("Self Test - FindList:", FindList(M,OPEN_LIST,CLOSE_LIST))
obstacle=GetBoundary(5)
print("Self Test - GetBoundary:\n", obstacle)
start_point=mat([[1,1]])
end_point=mat([[4,4]])
num=5
obstacle=GetObstacle(num,obstacle,start_point,end_point,5)
print("Self Test - GetObstacle:\n", obstacle)
e=mat([[4,2]])
print("Self Test - isObstacle:", isObstacle(e,obstacle))
start_point=mat([[1,1]])
end_point=mat([[4,4]])
print("Self Test - Astar:\n", Astar(obstacle,start_point,end_point))
# -*- coding: utf-8 -*-
import time
import matplotlib.pyplot as plt

def showResult(xList, yList, title, xLabel, yLabel):
    plt.plot(xList, yList, 'g*-')
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    for x, y in zip(xList, yList):
        plt.text(x, y+0.3, str(y), ha='center', va='bottom', fontsize=10.5)
        # plt.savefig('fig'+str(int(time.time()))+'.jpg')
        plt.draw()
        plt.pause(0.5)

x_arr = [1, 2, 3, 4, 5, 6]
y_arr = [1, 4, 9, 16, 25, 36]
showResult(x_arr, y_arr, 'title', 'x', 'y')

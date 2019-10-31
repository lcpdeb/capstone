#!/usr/bin/env python
# encoding: utf-8
from numpy import *
from isSamePosition import isSamePosition
from GetBoundary import GetBoundary

# WILL BE USED BY ULTRASONIC

def GetObstacle(num_of_obstacle,obstacle,start,goal,map_size):
    # generate Obstacles
    ob_cordinate=mat(random.randint(1,map_size+1,size=[map_size*map_size,2]))
    # print("obstacles are :\n", ob_cordinate)
    # pick #num_of_obstacle of obstacles generated
    ob=ob_cordinate[0:num_of_obstacle,:]
    # print("obstacles are :\n", ob)
    # remove Starting Point and Goal
    removed_list=[]
    for index in range(0,len(ob[:,0])):
        if isSamePosition(ob[index,:],start) or isSamePosition(ob[index,:],goal):
            # Add Start/Goal to Remove List
            removed_list.append(index)
    # Remove the element in Remove List in row
    ob=delete(ob,removed_list,axis=0)
    # Add Obstacle to the list
    obstacle=vstack((ob,obstacle))
    return obstacle

if __name__ == '__main__':
    start_point=mat([[1,1]])
    end_point=mat([[4,4]])
    num=5
    obstacle=mat([[0,0],
                  [1,0],
                  [2,0],
                  [3,0]])
    print("Unit Test - GetObstacle: \n", GetObstacle(num,obstacle,start_point,end_point,5))
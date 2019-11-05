#!/usr/bin/env python
# encoding: utf-8
from numpy import *
from isSamePosition import isSamePosition
from GetBoundary import GetBoundary
from Ultrasonic import Ultrasonic


# WILL BE USED BY ULTRASONIC

def random_pick(some_list, probabilities): 
    x = random.uniform(0,1)
    cumulative_probability = 0.0 
    for item, item_probability in zip(some_list, probabilities): 
         cumulative_probability += item_probability
         if x < cumulative_probability:
               break 
    return item 

def GetObstacle(path_map,mode):
    left_detect_flag=0
    right_detect_flag=0
    up_detect_flag=0
    down_detect_flag=0
    if mode=='random':
        # generate Obstacles
        new_obstacle_cordinate=mat(random.randint(1,path_map.map_size+1,size=[path_map.map_size*path_map.map_size,2]))
        # pick #num_of_obstacle of obstacles generated
        new_obstacle=new_obstacle_cordinate[0:path_map.num_of_obstacle,:]
        # remove Starting Point and Goal
        removed_list=[]
        for index in range(0,len(new_obstacle[:,0])):
            if isSamePosition(new_obstacle[index,:],path_map.start_position) or isSamePosition(new_obstacle[index,:],path_map.end_position):
                # Add Start/Goal to Remove List
                removed_list.append(index)
        # Remove the element in Remove List in row
        new_obstacle=delete(new_obstacle,removed_list,axis=0)
    elif mode=='detect':
        new_obstacle=mat([[0,0]])
        print("Ultrasonic is detecting...")
        
        # ultrasonic not created yet

        left_detect_flag,right_detect_flag,up_detect_flag,down_detect_flag=Ultrasonic(path_map)

        # simulation
        if left_detect_flag:
            temp_obstacle=mat([[path_map.current_position[0,0]-1,path_map.current_position[0,1]]])
            new_obstacle=vstack((new_obstacle,temp_obstacle))
        if right_detect_flag:
            temp_obstacle=mat([[path_map.current_position[0,0]+1,path_map.current_position[0,1]]])
            new_obstacle=vstack((new_obstacle,temp_obstacle))
        if up_detect_flag:
            temp_obstacle=mat([[path_map.current_position[0,0],path_map.current_position[0,1]+1]])
            new_obstacle=vstack((new_obstacle,temp_obstacle))
        if down_detect_flag:
            temp_obstacle=mat([[path_map.current_position[0,0],path_map.current_position[0,1]-1]])
            new_obstacle=vstack((new_obstacle,temp_obstacle))

        # # real situation
        # ultrasonic_detect_vector=mat(([left_detect_flag],
        #                               [right_detect_flag],
        #                               [up_detect_flag],
        #                               [down_detect_flag]))

        # obstacle_in_map=path_map.trasnmit_matrix*ultrasonic_detect_vector
        
        # if obstacle_in_map[0,0]:
        #     temp_obstacle=mat([[path_map.current_position[0,0]-1,path_map.current_position[0,1]]])
        #     new_obstacle=vstack((new_obstacle,temp_obstacle))
        # if obstacle_in_map[1,0]:
        #     temp_obstacle=mat([[path_map.current_position[0,0]+1,path_map.current_position[0,1]]])
        #     new_obstacle=vstack((new_obstacle,temp_obstacle))
        # if obstacle_in_map[2,0]:
        #     temp_obstacle=mat([[path_map.current_position[0,0],path_map.current_position[0,1]+1]])
        #     new_obstacle=vstack((new_obstacle,temp_obstacle))
        # if obstacle_in_map[3,0]:
        #     temp_obstacle=mat([[path_map.current_position[0,0],path_map.current_position[0,1]-1]])
        #     new_obstacle=vstack((new_obstacle,temp_obstacle))


        # remove first all-zero row 
        new_obstacle=delete(new_obstacle,0,axis=0)
        # print(new_obstacle)

    return new_obstacle

if __name__ == '__main__':
    from PATHPLANNING import pathplanning
    map_size=5
    start_position=mat([[1,1]])
    end_position=mat([[4,4]])
    path_map=pathplanning(start_position,end_position,map_size)
    path_map.current_position=path_map.start_position
    path_map.start_position=mat([[1,1]])
    path_map.end_position=mat([[4,4]])
    path_map.obstacle=mat([[0,0],
                           [1,0],
                           [2,0],
                           [3,0],
                           [1,2],
                           [2,1],
                           [0,1]])
    path_map.num_of_obstacle=5
    print("Unit Test - GetObstacle: \n", GetObstacle(path_map,mode='detect'))
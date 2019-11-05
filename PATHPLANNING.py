#!/usr/bin/env python
# encoding: utf-8
import time
from numpy import *
from Astar import Astar
from GetBoundary import GetBoundary
from GetObstacle import GetObstacle
from isObstacle import isObstacle
from isSamePosition import isSamePosition
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from Move import Move

class pathplanning:
    def __init__(self, start_position, end_position, map_size):
        self.start_position=start_position
        self.end_position=end_position
        self.map_size=map_size
        self.num_of_obstacle=3*self.map_size
 
        # generate map boundary, detected
        self.detected_obstacle=GetBoundary(self.map_size)

        # simulation
        # generate random OBSTACLE, undetected
        self.obstacle=GetObstacle(self,mode='random')
        # self.obstacle=vstack((self.obstacle,random_obstacle))
        # print("first undetected obstacle",self.obstacle)
        # print("first detected obstacle",self.detected_obstacle)
        # initialize the map plot
        self.plot=plt.gca()
        self.plot.set_xlim([0,self.map_size])
        self.plot.set_ylim([0,self.map_size])

        
    def UpdateObstacle(self,new_obstacle):
        try:
            self.detected_obstacle=vstack((self.detected_obstacle,new_obstacle))
            print("Obstacle updated.")
        except:
            print("No new obstacle detected.")

    def SaveImage(self,plt):    
        millis = int(round(time.time() * 1000))
        filename = './' + str(millis) + '.png'
        plt.savefig(filename)

    def UpdateOptimalPath(self):
        self.path=Astar(self.detected_obstacle,self.start_position,self.end_position)
        if self.path is not None:
            # reverse the OPTIMAL PATH
            self.path=self.path[::-1]
        else:
            return 1
        # print(self.path)

    def MapPlot(self):
        # draw the BOUNDARY and OBSTACLE
        for i in range(self.map_size+2):
            for j in range(self.map_size+2):
                if isObstacle(mat([[i,j]]), self.obstacle):
                    obstacle_plot=Rectangle((i+0.05, j+0.05), width=0.9, height=0.9, edgecolor='gray',facecolor=(0.88,0.88,0.88))
                    self.plot.add_patch(obstacle_plot)
                else:
                    empty_plot = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
                    self.plot.add_patch(empty_plot)
                
                if isObstacle(mat([[i,j]]), self.detected_obstacle):
                    detected_obstacle=Rectangle((i+0.05, j+0.05), width=0.9, height=0.9, edgecolor='white', facecolor='gray')
                    self.plot.add_patch(detected_obstacle)
        # legend
        plt.text(self.map_size+2.5, self.map_size-1.5, "Previous", size=10, va="center",bbox=dict(boxstyle="square",edgecolor='blue', facecolor='blue'))
        plt.text(self.map_size+2.5, self.map_size-3.0, "Path", size=10,  va="center",bbox=dict(boxstyle="square",edgecolor='green', facecolor='green'))
        plt.text(self.map_size+2.5, self.map_size-4.5, "Undetected", size=10, va="center",bbox=dict(boxstyle="round",edgecolor='gray', facecolor=(0.88,0.88,0.88)))
        plt.text(self.map_size+2.5, self.map_size-6.0, "Detected", size=10,  va="center",bbox=dict(boxstyle="round",edgecolor='white', facecolor='gray'))
        
        # draw the PREVIOUS POINT
        for i in range(len(self.previous_position)):
            previous_position_plot = Rectangle((self.previous_position[i,0]+0.25,self.previous_position[i,1]+0.25), 
                                                width = 0.5, height = 0.5, facecolor='blue')
            self.plot.add_patch(previous_position_plot)

        # draw the START POINT
        start_position_plot = Rectangle((self.start_position[0,0]+0.05,self.start_position[0,1]+0.05), 
                                            width = 0.9, height = 0.9, edgecolor='black', facecolor='blue')
        self.plot.add_patch(start_position_plot)
        plt.text(self.start_position[0,0]-1.3, self.start_position[0,1]+0.13, "START", ha='center', va='bottom', fontsize=10.5)

        # draw the direction arrow 
        plt.arrow(self.start_position[0,0]+0.5, self.start_position[0,1]+0.5, 
                    0.01*self.last_direction[0,0], 0.01*self.last_direction[0,1], 
                    head_length=0.5, head_width=0.5, edgecolor='black', facecolor='white')
        
        # draw the GOAL POINT
        end_position_plot = Rectangle((self.end_position[0,0]+0.05,self.end_position[0,1]+0.05), 
                                            width = 0.9, height = 0.9, edgecolor='black', facecolor='r')
        self.plot.add_patch(end_position_plot)
        plt.text(self.end_position[0,0]+2.2, self.end_position[0,1]+0.13, "GOAL", ha='center', va='bottom', fontsize=10.5)
        
        # set the axis of plot equally
        self.plot.axis('equal') 
        self.plot.axis('off')
    
    def PathPlot(self):
        plt.ion()
        # generate OPTIMAL PATH step by step
        for p in range(1,len(self.path[:,0])-1):
            path_plot=Rectangle((self.path[p,0]+0.25,self.path[p,1]+0.25),
                                        width = 0.5, height = 0.5, facecolor='g')
            self.plot.add_patch(path_plot)
            # print("Current Position is: ({},{})".format(self.path[p,0],self.path[p,1]))
            plt.draw()
        plt.pause(0.1)
        plt.cla()
        plt.ioff()



if __name__ == '__main__':
    map_size=20
    start_position=mat([[1,1]])
    end_position=mat([[map_size,map_size]])
    print("Unit Test - PATHPLANNING:")
     # generate BOUNDARY first
    capstone=pathplanning(start_position,end_position,map_size)
    capstone.current_position=capstone.start_position
    # LOOP:
    # print(not isSamePosition(capstone.current_position,capstone.end_position))
    break_flag=0
    capstone.previous_position=capstone.current_position
    capstone.last_direction=mat([[0,1]])
    capstone.trasnmit_matrix=mat([[1,0,0,0],
                                  [0,1,0,0],
                                  [0,0,1,0],
                                  [0,0,0,1]])
    while (not isSamePosition(capstone.current_position,capstone.end_position)):
        # detect whether OBSTACLE surrounded
        # get detected OBSTACLE
        detected_obstacle=GetObstacle(capstone,mode='detect')

        # # remove PREVIOUS POSITION as OBSTACLE
        # rmlist=[]
        # if len(detected_obstacle):
        #     for i in range(len(detected_obstacle)):
        #         for j in range(len(capstone.previous_position)):
        #             if isSamePosition(capstone.previous_position[j,:],detected_obstacle[i,:]):
        #                 rmlist.append(i)
        # detected_obstacle=delete(detected_obstacle,rmlist,axis=0)

        # Update OBSTACLE
        capstone.UpdateObstacle(detected_obstacle)
        # generate OPTIMAL PATH
        break_flag=capstone.UpdateOptimalPath()
        # if no path can reach GOAL, break
        if break_flag:
            break
        else:
            # plot map
            # print("Ploting...")
            capstone.MapPlot()
            plt.draw()
            # plot OPTIMAL PATH
            capstone.PathPlot()
            # MOVE ONE STEP
            capstone.next_position=capstone.path[1,:]
            capstone.current_position, capstone.trasnmit_matrix, capstone.last_direction=Move(capstone.last_direction, capstone.current_position,capstone.next_position)
            print("Moving...")
            # time.sleep(5)
            capstone.previous_position=vstack((capstone.current_position,capstone.previous_position))
            # prepare for next LOOP
            capstone.current_position=capstone.next_position
            capstone.start_position=capstone.current_position
    # LOOP END
    capstone.MapPlot()
    print("END")
    plt.show()
    
            
#!/usr/bin/env python
# encoding: utf-8
from numpy import *
from Astar import Astar
from GetBoundary import GetBoundary
from GetObstacle import GetObstacle
from isObstacle import isObstacle
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class pathplanning:
    def __init__(self, start_position, end_position, map_size, num_obstacle):
        self.start_position=start_position
        self.end_position=end_position
        self.map_size=map_size
        self.num_obstacle=num_obstacle

        # generate map boundary
        self.obstacle=GetBoundary(self.map_size)
        # update obstacles
        self.obstacle=GetObstacle(self.num_obstacle,self.obstacle,self.start_position,self.end_position,self.map_size)
        # get the OPTIMAL PATH
        self.path=Astar(self.obstacle,self.start_position,self.end_position)
        # reverse the OPTIMAL PATH
        self.path=self.path[::-1]
        print(self.path)

        self.plot=plt.gca()
        self.plot.set_xlim([0,self.map_size])
        self.plot.set_ylim([0,self.map_size])
        

    def SaveImage(self,plt):    
        millis = int(round(time.time() * 1000))
        filename = './' + str(millis) + '.png'
        plt.savefig(filename)

    def PathPlot(self):
        # draw the BOUNDARY and OBSTACLE
        for i in range(self.map_size+2):
            for j in range(self.map_size+2):
                if isObstacle(mat([[i,j]]),self.obstacle):
                    obstacle_plot=Rectangle((i, j), width=1, height=1, color='gray')
                    self.plot.add_patch(obstacle_plot)
                else:
                    empty_plot = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
                    self.plot.add_patch(empty_plot)
        start_position_plot = Rectangle((self.start_position[0,0],self.start_position[0,1]), 
                                            width = 1, height = 1, facecolor='b')
        self.plot.add_patch(start_position_plot)
        plt.text(self.start_position[0,0], self.start_position[0,1]+0.3, "START", ha='center', va='bottom', fontsize=10.5)
        end_position_plot = Rectangle((self.end_position[0,0],self.end_position[0,1]), 
                                            width = 1, height = 1, facecolor='r')
        self.plot.add_patch(end_position_plot)
        plt.text(self.end_position[0,0], self.end_position[0,1]+0.3, "GOAL", ha='center', va='bottom', fontsize=10.5)

        plt.axis('equal') 
        plt.axis('off')
        plt.tight_layout()
        if len(self.path[:,0]):
            for p in range(len(self.path[:,0])):
                print(self.path[p,0],self.path[p,1])
                path_plot=Rectangle((self.path[p,0],self.path[p,1]), 
                                            width = 1, height = 1, facecolor='g')
                self.plot.add_patch(path_plot)
                plt.draw()
                plt.pause(0.25)
        plt.show()



        


if __name__ == '__main__':
    map_size=10
    start_position=mat([[1,1]])
    end_position=mat([[map_size-1,map_size-1]])
    num=30
    print("Unit Test - PATHPLANNING:")
    try:
        pathplan=pathplanning(start_position,end_position,map_size,num)
        pathplan.PathPlot()
    except:
        pass

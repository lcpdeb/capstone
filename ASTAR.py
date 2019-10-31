from numpy import *
import time
from H import H
from isSamePosition import isSamePosition
from MotionModel import MotionModel
from FindList import FindList
from GetBoundary import GetBoundary
from GetObstacle import GetObstacle
from isObstacle import isObsatcle

def Astar(obstacle,start,goal):
    G=0 # NEXT MOVE cost
    path=[] # Create an empty path array
    open_list=mat([[start[0,0]],                # current position x
                   [start[0,1]],                # current position y
                   [G+H(start,goal)],           # total cost F=G+H, 当前点到终点的距离
                   [start[0,0]],                # last position x, parent set
                   [start[0,1]]]).transpose()   # last position y, parent set
    # initialize CLOSE LIST, this all-zero row will be removed after OPTIMAL PATH found
    close_list=mat([[0,0,0,0,0]])
    # open_list=mat([[0,0]])
    # open_list=delete(open_list,0,axis=0)
    next_move=MotionModel() # set NEXT position motion model
    findFlag=False # flag to determine whether the path can be found
    # print(open_list)

    while findFlag==False:
        # first column of OPEN LIST is empty
        if len(open_list)==0:
            print("No path to GOAL.")
            return

        # sorting open list based on total cost
        open_list=open_list[lexsort((open_list.view(ndarray)[:,2],))]
        # print(open_list)

        # compare the current position to GOAL position
        if isSamePosition(open_list[0,0:2],goal):
            print("Optimal path found.")
            # put first row of OPEN LIST into CLOSE LIST
            close_list=vstack((open_list[0,:],close_list))
            # remove the least cost MOVE from OPEN LIST
            open_list=delete(open_list,0,axis=0)
            findFlag=True
            break
        
        # calculate the cost in NEXT MOTION MODEL
        for index in range(0,len(next_move[:,0])):
            m=mat([[open_list[0,0]+next_move[index,0]], # pick NEXT MOVE position x
                [open_list[0,1]+next_move[index,1]], # pick NEXT MOVE position y
                [0]]).transpose()                    
            G=next_move[index,2]+H(m[0:2],goal) # NEXT MOVE cost G
            m[0,2]=G
            print("m =",m)

            # skip if current position is OBSTACLE
            if isObsatcle(m,obstacle):
                print("[{}, {}] is OBSTACLE".format(m[0,0],m[0,1]))
                continue

            # check that whether the next movement choice is in OPEN LIST or CLOSE LIST
            list_flag=FindList(m,open_list,close_list)
            print("list flag =",list_flag)
            # if it is in OPEN LIST or CLOSE LIST, skip
            if list_flag==1: # in OPEN LIST
                print("[{}, {}] is in OPEN LIST".format(m[0,0],m[0,1]))
                continue
            elif list_flag==2: # in CLOSE LIST
                print("[{}, {}] is in CLOSE LIST".format(m[0,0],m[0,1]))
                continue
            else:
                # append this MOVE and current position into OPEN LIST
                print("[{}, {}] has appended into OPEN LIST".format(m[0,0],m[0,1]))
                temp=hstack((m,[[open_list[0,0]]],[[open_list[0,1]]]))
                open_list=vstack((open_list,temp))
                print(open_list)

        # if the NEXT MOVE is neither in OPEN LIST nor CLOSE LIST
        if findFlag==False: 
            # append the least cost MOVE into CLOSE LIST, as moved
            close_list=vstack((open_list[0,:],close_list))
            print("[{}, {}] has added into PATH".format(close_list[0,0],close_list[0,1]))
            # remove the least cost MOVE from OPEN LIST
            open_list=delete(open_list,0,axis=0)

    # remove the last all-zero row in CLOSE LIST
    close_list=delete(close_list,-1,axis=0)
    print(close_list)

if __name__ == '__main__':
    start_point=mat([[1,1]])
    end_point=mat([[4,4]])
    obstacle=GetBoundary(5)
    print("Unit Test - Astar: ", Astar(obstacle,start_point,end_point))

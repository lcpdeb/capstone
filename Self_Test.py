from numpy import *
import time
from H import H
from isSamePosition import isSamePosition
from MotionModel import MotionModel
from FindList import FindList
from GetBoundary import GetBoundary
from GetObstacle import GetObstacle
from isObstacle import isObsatcle

a=mat([[3,4,5]])
b=mat([[4,5,6]])
print("Self Test - H cost: ", H(a,b))
c=mat([[1,2]])
d=mat([[1,2]])
print("Self Test - isSamePosition: ", isSamePosition(c,d))
print("Self Test - MotionModel: \n", MotionModel())
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
print("Self Test - FindList: ", FindList(M,OPEN_LIST,CLOSE_LIST))


# ob=mat([[3,3,3],
#         [4,4,4],
#         [5,5,5]])
# li=[0,2,0]
# ob=vstack((ob,li))
# print(ob)

# ob=delete(ob,li,axis=0)
# print(ob)
obstacle=GetBoundary(5)
print("Self Test - GetBoundary: \n", obstacle)
start_point=mat([[1,1]])
end_point=mat([[4,4]])
num=5
obstacle=GetObstacle(num,obstacle,start_point,end_point,5)
print("Self Test - GetObstacle: \n", obstacle)
e=mat([[4,2]])
print("Self Test - isObstacle: ", isObsatcle(e,obstacle))


f=mat([[3,4,5]])
g=[[4]]
h=[[5]]
print(hstack((f,g,h)))
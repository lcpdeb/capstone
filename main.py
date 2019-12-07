#!/usr/bin/env python
# encoding: utf-8
import time, threading
import RPi.GPIO as gpio
from LED import led_flash
from STEPPER import stepper
from numpy import *
from PATHPLANNING import pathplanning
from isSamePosition import isSamePosition
from GetBoundary import GetBoundary
from GetObstacle import GetObstacle
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from Move import Move
from GYROSCOPE import Gyro
# pin statement
#green_led_pin=17
#blue_led_pin=27

#ms1_pin=14
#ms2_pin=14
#ms3_pin=14
#enable_pin=14
#front_left_step_pin=26
#front_left_dir_pin=19
#back_left_dir_pin=13
#back_left_step_pin=6
#front_right_dir_pin=3
#front_right_step_pin=2
#back_right_dir_pin=27
#back_right_step_pin=17
## initialize
##led=led_flash(green_led_pin,blue_led_pin)
#front_left_stepper=stepper(front_left_step_pin,front_left_dir_pin,ms1_pin,ms2_pin,ms3_pin,enable_pin,0)
#back_left_stepper=stepper(back_left_step_pin,back_left_dir_pin,ms1_pin,ms2_pin,ms3_pin,enable_pin,0)
#front_right_stepper=stepper(front_right_step_pin,front_right_dir_pin,ms1_pin,ms2_pin,ms3_pin,enable_pin,0)
#back_right_stepper=stepper(back_right_step_pin,back_right_dir_pin,ms1_pin,ms2_pin,ms3_pin,enable_pin,0)
#
#threads=[]
#task1=threading.Thread(target=front_left_stepper.steps, args=(500,))
#threads.append(task1)
#task2=threading.Thread(target=back_left_stepper.steps, args=(500,))
#threads.append(task2)
#task3=threading.Thread(target=front_right_stepper.steps, args=(-500,))
#threads.append(task3)
#task4=threading.Thread(target=back_right_stepper.steps, args=(-500,))
#threads.append(task4)

if __name__ == '__main__':
#    print("RUNNING...")
#    try:
#        for t in threads:
#            t.setDaemon(True)
#            t.start()
#        t.join()
#    except KeyboardInterrupt:
#        RPi.GPIO.cleanup()
    gpio.cleanup()
    # Initialize stepper class
    ms1_pin=14
    ms2_pin=14
    ms3_pin=14
    enable_pin=14
    front_left_step_pin=26
    front_left_dir_pin=19

#    back_left_step_pin=6
#    back_left_dir_pin=13
    
    front_right_step_pin=17
    front_right_dir_pin=27

#    back_right_step_pin=17
#    back_right_dir_pin=27
    
    FRONT_LEFT=[front_left_step_pin, front_left_dir_pin]
    FRONT_RIGHT=[front_right_step_pin, front_right_dir_pin]
    BACK_LEFT=[]
    BAKC_RIGHT=[]
    capstone_gyro=Gyro(0x50)
    capstone_stepper=stepper(FRONT_LEFT,FRONT_RIGHT,BACK_LEFT,BAKC_RIGHT,ms1_pin,ms2_pin,ms3_pin,enable_pin,0, capstone_gyro)
    
    # Initialize Mapping
    map_size=5
    start_position=mat([[1,4]])
    end_position=mat([[1,2]])
    print("Capstone - path planning")
    # generate BOUNDARY first
    capstone=pathplanning(start_position,end_position,map_size)
    capstone.current_position=capstone.start_position
    # LOOP:
    # print(not isSamePosition(capstone.current_position,capstone.end_position))
    break_flag=0
    capstone.previous_position=capstone.current_position
    capstone.last_direction=mat([[0,1]])
    if (capstone.last_direction==mat([[0,-1]])).all():
        capstone.trasnmit_matrix=mat([[0,1,0,0],
                                      [1,0,0,0],
                                      [0,0,0,1],
                                      [0,0,1,0]])
        print('b')
    elif (capstone.last_direction==mat([[0,1]])).all():
        capstone.trasnmit_matrix=mat([[1,0,0,0],
                                      [0,1,0,0],
                                      [0,0,1,0],
                                      [0,0,0,1]])
        print('a')
    elif (capstone.last_direction==mat([[1,0]])).all():
        capstone.trasnmit_matrix=mat([[0,0,0,1],
                                      [0,0,1,0],
                                      [1,0,0,0],
                                      [0,1,0,0]])
    elif (capstone.last_direction==mat([[-1,0]])).all():
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
            capstone.current_position, capstone.trasnmit_matrix, capstone.last_direction=Move(capstone.last_direction, capstone.current_position,capstone.next_position, capstone_stepper)
            print("Moving...")
#            time.sleep(5)
            capstone.previous_position=vstack((capstone.current_position,capstone.previous_position))
            # prepare for next LOOP
            capstone.current_position=capstone.next_position
            capstone.start_position=capstone.current_position
    # LOOP END
    capstone.MapPlot()
    print("END")
    plt.show()
    
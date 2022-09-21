#!/usr/bin/python3
from re import I
from time import time
import numpy as np
import rospy
from mycobot.msg import joint
import cv2
import os

startTime = 0
z = 120
query = ""
x = 1 
captureTime = 0
g = False
state = True
name = ""
nodecommunication = False
def callback(joints):
    global userInput
    global startTime
    global captureTime 
    global x
    global j1array
    global j2array
    global j3array
    global j4array
    global j5array
    global j6array
    global j7array
    global g
    global z
    global timeleft
    global keys
    global state
    global name
    global query
    global nodecommunication 

    nodecommunication =True
    while userInput == 0: 
        
        if state == True:
            print("Press 'r' to START recording PICK CUP trajectory")
            name = "PICK TEACUP"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        if keys == ord('r'):
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 1
    
    while userInput == 2:
        if state ==True:
            print("Press 'r' to START recording PLACE CUP trajectory")
            name = "PLACE TEACUP"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 3
    
    while userInput == 4:
        if state ==True:
            print("Press 'r' to START recording PICK TEABAG trajectory")
            name = "PICK TEABAG"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 5
    
    while userInput == 6:
        if state ==True:
            print("Press 'r' to START recording PLACE TEABAG trajectory")
            name = "PLACE TEABAG"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 7
    
    while userInput == 8:
        if state ==True:
            print("Press 'r' to START recording PICK WATER trajectory")
            name = "PICK WATERCUP"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 9
        
    while userInput == 10:
        if state ==True:
            print("Press 'r' to START recording LOCATE WATER trajectory")
            name = "LOCATE WATERCUP"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 11
    
    while userInput == 12:
        if state ==True:
            print("Press 'r' to START recording POUR WATER trajectory")
            name = "POUR WATER"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 13
    
    while userInput == 14:
        if state ==True:
            print("Press 'r' to START recording PLACE WATER trajectory")
            name = "PLACE WATERCUP"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 15
    
    while userInput == 16:
        if state ==True:
            print("Press 'r' to START recording PICK SPOON trajectory")
            name = "PICK SPOON"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 17
    
    while userInput == 18:
        if state ==True:
            print("Press 'r' to START recording LOCATE SPOON trajectory")
            name = "LOCATE SPOON"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 19
    
    while userInput == 20:
        if state ==True:
            print("Press 'r' to START recording STIR trajectory")
            name = "STIR SPOON"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 21
    
    while userInput == 22:
        if state ==True:
            print("Press 'r' to START recording PLACE SPOON trajectory")
            name = "PLACE SPOON"
            query= "READY??"
            z = 120
            j1array = np.zeros((z,2))  
            j2array = np.zeros((z,2))  
            j3array = np.zeros((z,2))  
            j4array = np.zeros((z,2))  
            j5array = np.zeros((z,2))  
            j6array = np.zeros((z,2))  
            j7array = np.zeros((z,2))
            state = False
        # if keys == ord('r'):
        if rospy.get_time() - startTime > 3:
            query= "RECORDING!!"
            startTime = rospy.get_time() 
            captureTime = rospy.get_time()
            userInput = 23 
    
    if  (rospy.get_time()-startTime) >= 0.5 and  x < z:
        
        j1array[x][1] = joints.data[0]
        j2array[x][1] = joints.data[1]
        j3array[x][1] = joints.data[2]
        j4array[x][1] = joints.data[3]
        j5array[x][1] = joints.data[4]
        j6array[x][1] = joints.data[5]
        
        def map_range(x, in_min, in_max, out_min, out_max):
            return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
        
        j7array[x][1] = map_range(joints.data[6],1450,2000,0,5)

        j1array[x][0] = rospy.get_time()-captureTime
        j2array[x][0] = rospy.get_time()-captureTime
        j3array[x][0] = rospy.get_time()-captureTime
        j4array[x][0] = rospy.get_time()-captureTime
        j5array[x][0] = rospy.get_time()-captureTime
        j6array[x][0] = rospy.get_time()-captureTime
        j7array[x][0] = rospy.get_time()-captureTime
        
        
        timeleft = z*0.5-(rospy.get_time()-captureTime)
        if timeleft <= 0:
            timeleft = 0
        # print("TIME REMAINING TO RECORD {}".format(timeleft))
        x += 1
        startTime = rospy.get_time() 
    
    # print("J1ARRAY!!!")
    # print(j1array)

    # print("J2ARRAY!!!")
    # print(j2array)
    
    # print("J3ARRAY!!!")
    # print(j3array)

    # print("J4ARRAY!!!")
    # print(j4array)
    
    # print("J5ARRAY!!!")
    # print(j5array)

    # print("J6ARRAY!!!")
    # print(j6array)
    
    # print("J7ARRAY!!!")
    # print(j7array)


    if x == z and userInput == 1:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPICK_CUP',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPICK_CUP',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPICK_CUP',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPICK_CUP',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPICK_CUP',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPICK_CUP',j6array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j7trajPICK_CUP',j7array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/PICK_CUP_FinalJoints',finaljointarray)
        print("PICK CUP TRAJECTORY CAPTURED SHUTTING DOWN!")
        
        x=1
        state = True
        userInput=2
    
    elif x == z and userInput == 3:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPLACE_CUP',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPLACE_CUP',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPLACE_CUP',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPLACE_CUP',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPLACE_CUP',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPLACE_CUP',j6array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j7trajPLACE_CUP',j7array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/PLACE_CUP_FinalJoints',finaljointarray)
        print("PLACE CUP TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=4
        
    elif x == z and userInput == 5:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPICK_TEA',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPICK_TEA',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPICK_TEA',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPICK_TEA',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPICK_TEA',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPICK_TEA',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/PICK_TEA_FinalJoints',finaljointarray)
        print("PICK TEA TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=6
    
    elif x == z and userInput == 7:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPLACE_TEA',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPLACE_TEA',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPLACE_TEA',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPLACE_TEA',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPLACE_TEA',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPLACE_TEA',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/PLACE_TEA_FinalJoints',finaljointarray)
        print("PLACE TEA TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=8
        
    elif x == z and userInput == 9:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPICK_H20',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPICK_H20',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPICK_H20',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPICK_H20',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPICK_H20',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPICK_H20',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/PICK_H20_FinalJoints',finaljointarray)
        print("PICK H20 TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=10
    
    elif x == z and userInput == 11:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajLOCATE_H20',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajLOCATE_H20',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajLOCATE_H20',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajLOCATE_H20',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajLOCATE_H20',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajLOCATE_H20',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/LOCATE_H20_FinalJoints',finaljointarray)
        print("LOCATE H20 TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=12 
    
    elif x == z and userInput == 13:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPOUR_H20',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPOUR_H20',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPOUR_H20',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPOUR_H20',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPOUR_H20',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPOUR_H20',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/POUR_H20_FinalJoints',finaljointarray)
        print("POUR H20 TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        startTime = rospy.get_time()
        state = True
        userInput=14 
    
    elif x == z and userInput == 15:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPLACE_H20',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPLACE_H20',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPLACE_H20',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPLACE_H20',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPLACE_H20',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPLACE_H20',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/PLACE_H20_FinalJoints',finaljointarray)
        print("PLACE H20 TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=16 
    
    
    elif x == z and userInput == 17:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPICK_SPOON',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPICK_SPOON',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPICK_SPOON',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPICK_SPOON',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPICK_SPOON',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPICK_SPOON',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/PICK_SPOON_FinalJoints',finaljointarray)
        print("PICK SPOON TRAJECTORY CAPTURED SHUTTING DOWN!")
        print("TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=18    
        
    elif x == z and userInput == 19:   
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajLOCATE_SPOON',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajLOCATE_SPOON',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajLOCATE_SPOON',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajLOCATE_SPOON',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajLOCATE_SPOON',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajLOCATE_SPOON',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/LOCATE_SPOON_FinalJoints',finaljointarray)
        print("LOCATE SPOON TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=20    
    
    elif x == z and userInput == 21:
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajSTIR_SPOON',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajSTIR_SPOON',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajSTIR_SPOON',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajSTIR_SPOON',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajSTIR_SPOON',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajSTIR_SPOON',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/STIR_SPOON_FinalJoints',finaljointarray)
        print("STIR SPOON TRAJECTORY CAPTURED SHUTTING DOWN!")
        x=1
        state = True
        startTime = rospy.get_time()
        userInput=22    
        
    elif x == z and userInput == 23:    
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j1trajPLACE_SPOON',j1array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j2trajPLACE_SPOON',j2array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j3trajPLACE_SPOON',j3array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j4trajPLACE_SPOON',j4array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j5trajPLACE_SPOON',j5array)
        np.save('/home/aaron/catkin_ws/src/mycobot/data/j6trajPLACE_SPOON',j6array)
        finaljointarray = np.array([j1array[z-1][1],j2array[z-1][1],j3array[z-1][1],
                                    j4array[z-1][1],j5array[z-1][1],j6array[z-1][1]])
        np.save('/home/aaron/catkin_ws/src/mycobot/data/PLACE_SPOON_FinalJoints',finaljointarray)
        print("PLACE SPOON TRAJECTORY CAPTURED SHUTTING DOWN!")
        query = "Done"
        userInput =24
        
        
def main(): 
    global keys
    global userInput
    global z
    global name
    global query
    global capL
    rospy.init_node('traj_recorder',anonymous=True)
    # Subscribes to topic called joint_state published by rviz
    
    # Opening camera map parameters to undistort and rectify images
    cv_file = cv2.FileStorage()

    # Opends camera calibration parameters
    cv_file.open('/home/aaron/catkin_ws/src/mycobot/data/CameraCalibration.xml', cv2.FileStorage_READ)
    # Asssigning variables from xml file
    LcameraMatrix = cv_file.getNode('LcameraMatrix').mat()
    LnewCameraMatrix = cv_file.getNode('LnewCameraMatrix').mat()
    distL = cv_file.getNode('LdistCoeffs').mat()
 
    #Capture the video from webcam
    capL = cv2.VideoCapture(1)

    #Gets the camera parameters and prints it to terminal
    print("Frame incoming resolution: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")
    capL.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capL.set(cv2.CAP_PROP_FRAME_HEIGHT, 1980)
    print("Frame resolution set to: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")
    
    #Error checking
    if(capL.isOpened() == False):
        print("Error opening the video file")
    else:
        os.system("v4l2-ctl --device /dev/video1 -c focus_auto=0") 
        os.system("v4l2-ctl --device /dev/video1 -c focus_absolute=0")

    while capL.isOpened():
        
        #Read the incoming images
        success1,Limg = capL.read()
        #Rotate the images
        # Limg = (cv2.rotate(Limg,cv2.ROTATE_90_COUNTERCLOCKWISE))
        h,w = Limg.shape[:2]
        # Undistort with Remapping
        mapxL, mapyL = cv2.initUndistortRectifyMap(LcameraMatrix, distL, None, LnewCameraMatrix, (w,h), 5)
        Limg = cv2.remap(Limg, mapxL, mapyL, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT,0)
       
    
        #Window name location and size parameters
        cv2.namedWindow("CAM",cv2.WINDOW_NORMAL)
        # cv2.resizeWindow("CAM", 900, 900)

       
        
        keys = cv2.waitKey(1) & 0xFF
        
        #Wait ms between frames and if q is pressed break the while loop
        if keys == ord('q'):
            break
        
        font                      = cv2.FONT_HERSHEY_SIMPLEX
        locationText = (0,1040)
        fontScale              = 4
        fontColor              = (0,0,255)
        thickness              = 5
        lineType               = 1 
        if nodecommunication == True:
            
            cv2.putText(Limg,"Time Left: {}".format(round(int(timeleft),2)), locationText,font,fontScale,fontColor,thickness,lineType)
            cv2.putText(Limg,name+": {} secs".format(round(z/2)),(0,840),font,fontScale,(255,0,0),thickness,lineType)
            
            if query == "READY??":
                fontColor=(0,255,0)
            else:
                fontColor=(0,0,255)   
            cv2.putText(Limg,query,(900,120),font,fontScale,fontColor,thickness,lineType)
            
        else:
            cv2.putText(Limg,"ROS JOINT COMMUNICATION",(0,120),font,fontScale,fontColor,thickness,lineType)
            cv2.putText(Limg,"NODE NOT ACTIVE",(0,320),font,fontScale,fontColor,thickness,lineType)
        rospy.Subscriber("/cobot_joints",joint,callback)
        
        # Display the Image
        cv2.imshow("CAM",Limg)
        
        if query == "Done":    
            # # Release webcam feeds and close all windows   
            break

    capL.release()
    cv2.destroyAllWindows()     
    rospy.signal_shutdown("Finished Recording")
  
    
if __name__ == '__main__':
    global userInput
    global timeleft
    timeleft = 0
    userInput = 0
    # Array used to store info from images processed  
   
    
     
    main()
    

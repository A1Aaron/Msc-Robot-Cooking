import sys
import copy
from turtle import st
from matplotlib.pyplot import step
from sympy import true
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import numpy as np
from math import pi, tau, dist, fabs, cos
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from moveit_commander.conversions import pose_to_list
from tf.transformations import euler_from_quaternion, quaternion_from_euler

timeon = 0
active = True 
capturetime = 0.1
steparray = 2
stepdistance = 0.01
stepDistance = stepdistance
Rstepdistance = pi/12
RstepDistance = Rstepdistance
toggle = False
spacenavb1old = 0
toggle2 = False
begin = True
includeorientation = False
    
# Function to convert euler to quaternion
def eulerTOquart(roll,pitch,yaw):
    (qx, qy, qz, qw) = quaternion_from_euler(roll,pitch,yaw)
    return qx,qy,qz,qw

# Function to convert quaternion to euler
def quartTOeuler(msg):
    global roll, pitch, yaw
    orientation_q = msg.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    return roll,pitch,yaw

# Callback function after incoming Joy message recived from spacnavtopic
def callback(posemsg):
    # Initalising Variables 
    global timeon
    global active
    global X
    global Y
    global Z
    global Rx
    global Ry
    global Rz
    global rx
    global ry
    global rz
    global i
    global points
    global capturetime
    global stepdistance
    global stepDistance
    global steparray
    global toggle
    global spacenavb1old
    global toggle2
    global spacenavb2old
    global Rstepdistance
    global RstepDistance
    global includeorientation
    global begin

    mousethreshold = 0.68
    spacenavy = posemsg.axes[0]
    spacenavx = posemsg.axes[1]
    spacenavz = posemsg.axes[2]
    spacenavRy = posemsg.axes[3]
    spacenavRx = posemsg.axes[4]
    spacenavRz = posemsg.axes[5]
    spacenavb1 = posemsg.buttons[0]
    spacenavb2 = posemsg.buttons[1]
    
    if begin == True:
        print("============Initial========== Printing robot state")
        print(move_grouparm.get_current_pose())
        print("")
        X = move_grouparm.get_current_pose()
        Y = move_grouparm.get_current_pose()
        Z = move_grouparm.get_current_pose()
        rx,ry,rz = quartTOeuler(move_grouparm.get_current_pose().pose)
        print("Initial Rotation: {}, {}, {}".format(rx,ry,rz))
        begin = False
  
    # If spacenavebutton1 has a chnage of state from 0 to 1
    if(spacenavb1 == 1 and spacenavb1old == 0):
        # toggle between states
        toggle = not toggle
        # If toggle is false stepdistance stays the same 
        if toggle == False:
            stepDistance = stepdistance
        # Else step distance is 10x greater
        else:
            stepDistance = stepdistance*10
    
    # Makes the old button to match new button state needed to aviod looping
    spacenavb1old = spacenavb1
   
   
   # If spacenavebutton2 has a chnage of state from 0 to 1
    if(spacenavb2 == 1 and spacenavb2old == 0):
        # toggle between states
        toggle2 = not toggle2
        # If toggle2 is false stepdistance stays the same 
        if toggle2 == False:
            RstepDistance = Rstepdistance
        # Else Rstep distance is 3x greater
        else:
            RstepDistance = Rstepdistance*6
    
    # Makes the old button to match new button state needed to aviod looping
    spacenavb2old = spacenavb2
   
        
    # print("Current:   " + str(spacenavb2) + "      Old:      "+str(spacenavb2old) +"          StepDistance:     "+str(RstepDistance))
    
    
     ################################## X MOVEMENT  ######################################
    # When the x position has exceed max mouse threshold
    if (spacenavx <= -mousethreshold):
        
        # If the mouse is active
        if active == True: 
            points = []
            # Capture the current x posisiton
            X = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(X.pose))
            print("Current X position of robot {}".format(X.pose.position.x)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniitial point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            # Positively increment the x posision by stepdistance
            X.pose.position.x += stepDistance
            # Adds the new incremented x position to the waypoint array
            points.append(copy.deepcopy(X.pose))
            # Records how many increments were made
            i+=1
            print(points) 
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()
            
    # When the x position has exceed min mouse threshold        
    elif (spacenavx >= mousethreshold):
        
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current x posisiton
            X = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(X.pose))
            print("Current X position of robot {}".format(X.pose.position.x)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniitial point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            # Negatively Increment the x posision by stepdistance
            X.pose.position.x -= stepDistance
            # Adds the new incremented x position to the waypoint array
            points.append(copy.deepcopy(X.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()
            
     ################################## Y MOVEMENT ################################################# 
    # When the yposition has exceed max mouse threshold
    elif (spacenavy >= mousethreshold):
        
        # If the mouse is active
        if active == True: 
            points = []
            # Capture the current y position
            Y = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Y.pose))
            print("Current Y position of robot {}".format(Y.pose.position.y)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            # Positively increment the y position by stepdistance
            Y.pose.position.y += stepDistance
            # Adds the new incremented x position to the waypoint array
            points.append(copy.deepcopy(Y.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()
            
    # When the y position has exceed min mouse threshold
    elif (spacenavy <= -mousethreshold):
        
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current y posisiton
            Y = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Y.pose))
            print("Current Y position of robot {}".format(Y.pose.position.y)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            # Negatively Increment the y posision by stepdistance
            Y.pose.position.y -= stepDistance
            # Adds the new incremented x position to the waypoint array
            points.append(copy.deepcopy(Y.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()
            
    ################################## Z MOVEMENT #######################################
    # When the z position has exceed max mouse threshold
    elif (spacenavz >= mousethreshold):
        
        # If the mouse is active
        if active == True: 
            points = []
            # Capture the current z posisiton
            Z = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Z.pose))
            print("Current Z position of robot {}".format(Z.pose.position.z)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            # Positively increment the z posision by stepdistance
            Z.pose.position.z += stepDistance
            # Adds the new incremented x position to the waypoint array
            points.append(copy.deepcopy(Z.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()
            
    # When the z position has exceed min mouse threshold        
    elif (spacenavz <= -mousethreshold):
        
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current z posisiton
            Z = move_grouparm.get_current_pose()
            # Add the curent position to the waypoints array
            points.append(copy.deepcopy(Z.pose))
            print("Current Z position of robot {}".format(Z.pose.position.z)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            # Negatively Increment the z position by stepdistance
            Z.pose.position.z -= stepDistance
            # Adds the new incremented x position to the waypoint array
            points.append(copy.deepcopy(Z.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()   
            
     
    ################################################### ROTATIONAL ###############################################################
     
     
    ####################################### ROLL RX ############################################### 
     
    # When the Rx position has exceed max mouse threshold        
    elif (spacenavRx <= -mousethreshold):
        includeorientation = True
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current pose 
            Rx = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Rx.pose))
            # Convert quarternions to eurlers and capture the roll
            rx,ry,rz = quartTOeuler(Rx.pose)
            print("Current Rx (roll) position of robot {}".format(rx)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            #Increment the Rx posision by stepdistance
            rx += RstepDistance
            # Convert back to quaternions and update pose
            qx,qy,qz,qw = eulerTOquart(rx,ry,rz)
            Rx.pose.orientation.x = qx
            Rx.pose.orientation.y = qy
            Rx.pose.orientation.z = qz
            Rx.pose.orientation.w = qw
            # Adds the new incremented Rx position to the waypoint array
            points.append(copy.deepcopy(Rx.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()       
            
            
            
    # When the Rx position has exceed min mouse threshold        
    elif (spacenavRx >= mousethreshold):
        includeorientation = True
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current pose 
            Rx = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Rx.pose))
            # Convert quarternions to eurlers and capture the roll
            rx,ry,rz = quartTOeuler(Rx.pose)
            print("Current Rx (roll) position of robot {}".format(rx)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            #Increment the Rx posision by stepdistance
            rx -= RstepDistance
            # Convert back to quaternions and update pose
            qx,qy,qz,qw = eulerTOquart(rx,ry,rz)
            Rx.pose.orientation.x = qx
            Rx.pose.orientation.y = qy
            Rx.pose.orientation.z = qz
            Rx.pose.orientation.w = qw
            # Adds the new incremented Rx position to the waypoint array
            points.append(copy.deepcopy(Rx.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()     
            
            
            
            ####################################### PITCH RY ############################################### 
     
    # When the Ry position has exceed max mouse threshold        
    elif (spacenavRy >= mousethreshold):
        includeorientation = True
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current pose 
            Ry = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Ry.pose))
            # Convert quarternions to eurlers and capture the roll
            rx,ry,rz = quartTOeuler(Ry.pose)
            print("Current Ry (pitch) position of robot {}".format(ry)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            #Increment the Ry posision by stepdistance
            ry += RstepDistance
            if ry > 1.57:
                ry = -1.56
            # Convert back to quaternions and update pose
            qx,qy,qz,qw = eulerTOquart(rx,ry,rz)
            Ry.pose.orientation.x = qx
            Ry.pose.orientation.y = qy
            Ry.pose.orientation.z = qz
            Ry.pose.orientation.w = qw
            # Adds the new incremented Ry position to the waypoint array
            points.append(copy.deepcopy(Ry.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()       
            
            
            
    # When the Ry position has exceed min mouse threshold        
    elif (spacenavRy <= -mousethreshold):
        includeorientation = True
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current pose 
            Ry = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Ry.pose))
            # Convert quarternions to eurlers and capture the pitch
            rx,ry,rz = quartTOeuler(Ry.pose)
            print("Current Ry (pitch) position of robot {}".format(ry)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            #Increment the Ry posision by stepdistance
            ry -= RstepDistance
            # Convert back to quaternions and update pose
            qx,qy,qz,qw = eulerTOquart(rx,ry,rz)
            Ry.pose.orientation.x = qx
            Ry.pose.orientation.y = qy
            Ry.pose.orientation.z = qz
            Ry.pose.orientation.w = qw
            # Adds the new incremented Ry position to the waypoint array
            points.append(copy.deepcopy(Ry.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()     
            
            
             ####################################### YAW RZ ############################################### 
     
    # When the Rz position has exceed max mouse threshold        
    elif (spacenavRz >= mousethreshold):
        includeorientation = True
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current pose 
            Rz = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Rz.pose))
            # Convert quarternions to eurlers and capture the roll
            rx,ry,rz = quartTOeuler(Rz.pose)
            print("Current Rz (yaw) position of robot {}".format(rz)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            #Increment the Ry posision by stepdistance
            rz += RstepDistance
            # Convert back to quaternions and update pose
            qx,qy,qz,qw = eulerTOquart(rx,ry,rz)
            Rz.pose.orientation.x = qx
            Rz.pose.orientation.y = qy
            Rz.pose.orientation.z = qz
            Rz.pose.orientation.w = qw
            # Adds the new incremented Rz position to the waypoint array
            points.append(copy.deepcopy(Rz.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()       
            
            
            
    # When the Rx position has exceed min mouse threshold        
    elif (spacenavRz <= -mousethreshold):
        includeorientation = True
         # If the mouse is active
        if active == True: 
            points = []
            # Capture the current pose 
            Rz = move_grouparm.get_current_pose()
            # Add the curent posision to the waypoints array
            points.append(copy.deepcopy(Rz.pose))
            # Convert quarternions to eurlers and capture the pitch
            rx,ry,rz = quartTOeuler(Rz.pose)
            print("Current Rz (yaw) position of robot {}".format(rz)) 
            # Get the time when moouse has reached threshold
            timeon = rospy.get_time()
            # Step array set to 1
            i = 1
            # active set to false to avoid overiding iniital point and time
            active = False
            
        # if the time since the mouse threhshold has exceeded capturetime and i is less than array size  
        if rospy.get_time() - timeon >= capturetime and i < steparray:
            #Increment the Ry posision by stepdistance
            rz -= RstepDistance
            # Convert back to quaternions and update pose
            qx,qy,qz,qw = eulerTOquart(rx,ry,rz)
            Rz.pose.orientation.x = qx
            Rz.pose.orientation.y = qy
            Rz.pose.orientation.z = qz
            Rz.pose.orientation.w = qw
            # Adds the new incremented Rz position to the waypoint array
            points.append(copy.deepcopy(Rz.pose))
            # Records how many increments were made
            i+=1
            print(points)  
            print("Rotation x:{}, y:{}, z:{}".format(rx,ry,rz))
            # resets the timeon variable to create a loop while threshold is active
            timeon = rospy.get_time()     
            
            
    ############# PLAN AND EXECUTE ###################        
    else: 
        # If the mouse is no longer activated and all specified points are captured plan and execute
        if active == False and i == steparray:
            goal = geometry_msgs.msg.Pose()
            goal.position.x = X.pose.position.x
            goal.position.y = Y.pose.position.y
            goal.position.z = Z.pose.position.z
            if includeorientation == True:
                goal.orientation.x, goal.orientation.y, goal.orientation.z, goal.orientation.w = eulerTOquart(rx,ry,rz)
            move_grouparm.set_pose_target(goal)
            plan = move_grouparm.go(wait=True)
            move_grouparm.stop()
            move_grouparm.clear_pose_targets()
            active = True
            includeorientation = True
            begin = True
    
    
    
    
        
        
        
# Function to convert quaternion to euler
def get_rotation (msg):
    global roll, pitch, yaw
    orientation_q = msg.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    print(roll,pitch,yaw)

# Initalise move it commander
moveit_commander.roscpp_initialize(sys.argv)
# Create a node 
rospy.init_node("move_group_python_interface", anonymous=True)
# Creates a robot object provides robot infomation
robot = moveit_commander.RobotCommander()
# Creeates a scene object provides scene infomation
scene = moveit_commander.PlanningSceneInterface()
# Defines the group names
group_name_arm = "arm"
# group_name_gripper = "gripper"
# Instantiates moveitgroupcommander opject usd for path planning
move_grouparm = moveit_commander.MoveGroupCommander(group_name_arm)
# move_groupgripper = moveit_commander.MoveGroupCommander(group_name_gripper)
# Creates a display publisher used to visulize movements in rviz
display_trajectory_publisher = rospy.Publisher(
    "/move_group/display_planned_path",
    moveit_msgs.msg.DisplayTrajectory,
    queue_size=20,
)
rospy.Subscriber("spacenav/joy",Joy,callback)


move_grouparm.set_planning_time(5)
move_grouparm.set_goal_orientation_tolerance(0.01)
move_grouparm.set_max_velocity_scaling_factor(1)
move_grouparm.set_max_acceleration_scaling_factor(1)

# USED FOR KEYBOARD POSITION ENTRY
# while not rospy.is_shutdown():
   
    
#     # Function to convert euler to quaternion
#     def get_rotation (roll,pitch,yaw):
#         (qx, qy, qz, qw) = quaternion_from_euler(roll,pitch,yaw)
#         return qx,qy,qz,qw
    
#     # Function to convert quaternion to euker
#     def get_Rotation (msg):
#         global roll, pitch, yaw
#         orientation_q = msg.pose.orientation
#         orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
#         (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
#         print(roll,pitch,yaw)
    
#     print("============Initial========== Printing robot state")
#     print(move_grouparm.get_current_pose())
#     print("")
#     get_Rotation(move_grouparm.get_current_pose())
#     Goal = input("Enter goal in x,y,z,rx,ry,rz format").split(',')
#     goal = geometry_msgs.msg.Pose()
    
#     if np.size(Goal)>3:
#         goal.orientation.x, goal.orientation.y, goal.orientation.z, goal.orientation.w = get_rotation(float(Goal[3]),float(Goal[4]),float(Goal[5]))
#         goal.position.x = float(Goal[0])
#         goal.position.y = float(Goal[1])
#         goal.position.z = float(Goal[2])
#         move_grouparm.set_pose_target(goal)
#         plan = move_grouparm.go(wait=True)
#         move_grouparm.stop()
#         move_grouparm.clear_pose_targets()
#         rospy.sleep(1)
#     else:
#         goal.position.x = float(Goal[0])
#         goal.position.y = float(Goal[1])
#         goal.position.z = float(Goal[2])
#         move_grouparm.set_pose_target(goal)
#         plan = move_grouparm.go(wait=True)
#         move_grouparm.stop()
#         move_grouparm.clear_pose_targets()
#         rospy.sleep(1)



rospy.spin()



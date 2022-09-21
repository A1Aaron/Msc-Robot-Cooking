from curses.panel import new_panel
import imp
from math import fabs
from ntpath import join
from operator import imod
from re import I
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import numpy as np
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import PickCupGeneration 
import PlaceCupGeneration
import PickTeaGeneration
import PlaceTeaGeneration
import PickH20Generation
import LocateH20Generation
import PourH20Generation
import PlaceH20Generation
import PickSpoonGeneration
import LocateSpoonGeneration
import StirSpoonGeneration
import PlaceSpoonGeneration

plan = False
Goal = np.zeros(6)   
def plan(xpos,ypos,zpos,rxpos,rypos,rzpos,int):
    global plan    
    global Goal
    Goal[0]=xpos
    Goal[1]=ypos
    Goal[2]=zpos
    Goal[3]=rxpos
    Goal[4]=rypos
    Goal[5]=rzpos
 

        
    
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
        queue_size=20,)
    
    move_grouparm.set_planning_time(3)
    move_grouparm.set_goal_orientation_tolerance(0.01)
    move_grouparm.set_goal_position_tolerance(0.001)
    move_grouparm.set_max_velocity_scaling_factor(1)
    move_grouparm.set_max_acceleration_scaling_factor(1)
    



   


    # USED FOR KEYBOARD POSITION ENTRY
    while not rospy.is_shutdown():
    
        
        # Function to convert euler to quaternion
        def get_rotation (roll,pitch,yaw):
            (qx, qy, qz, qw) = quaternion_from_euler(roll,pitch,yaw)
            return qx,qy,qz,qw
        
        # Function to convert quaternion to euker
        def get_Rotation (msg):
            global roll, pitch, yaw
            orientation_q = msg.pose.orientation
            orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
            (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
            print(roll,pitch,yaw)
        
        def go(): 
            global plan
            print("============Initial========== Printing robot state")
            print(move_grouparm.get_current_pose())
            print("")
            get_Rotation(move_grouparm.get_current_pose())
            goal = geometry_msgs.msg.Pose()
            goal.orientation.x, goal.orientation.y, goal.orientation.z, goal.orientation.w = get_rotation(float(Goal[3]),float(Goal[4]),float(Goal[5]))
            goal.position.x = float(Goal[0])
            goal.position.y = float(Goal[1])
            goal.position.z = float(Goal[2])
            print(Goal)
            move_grouparm.set_pose_target(goal)
            plan = move_grouparm.go(wait=True)
            move_grouparm.stop()
            move_grouparm.clear_pose_targets()
            
       
        
        
        go()
        print(plan)
        
        if int == 1 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PickCupGeneration.main(target=True,graph=True)
            break
        elif int == 1 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break
                
                
        if int == 2 and plan == True:
            
            
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PlaceCupGeneration.main(target=False,graph=False)
            break
        elif int == 2 and plan == False:
            # move_grouparm.set_goal_orientation_tolerance(1000)
            capgoal = Goal[5]
            y=0
            while (True):
                if y == 0:
                    Goal[5] -= 0.339
                    if Goal[5] < -3.14:
                        Goal [5]= 3.14
                #     if 0.95 <= Goal[5]/capgoal <= 1.05:
                #         y = 1
                # elif y == 1:
                #     Goal[4] -= 0.339
                #     if Goal[4] < -3.14:
                #         Goal [4]= 3.14   
                
                go()
                print(plan)
                if plan == True:
                    break


        if int == 3 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PickTeaGeneration.main(target=True,graph=True)
            break
        elif int == 3 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break
        
        
        if int == 4 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PlaceTeaGeneration.main(target=False,graph=False)
            break
        elif int == 4 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break
                
                
        if int == 5 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PickH20Generation.main(target=True,graph=True)
            break
        elif int == 5 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break 


        if int == 6 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            LocateH20Generation.main(target=False,graph=False)
            break
        elif int == 6 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break 
   
   
        if int == 7 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PourH20Generation.main(target=False,graph=False)
            break
        elif int == 7 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break 
                
        if int == 8 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PlaceH20Generation.main(target=False,graph=False)
            break
        elif int == 8 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break  
        
        if int == 9 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PickSpoonGeneration.main(target=True,graph=True)
            break
        elif int == 9 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break   
                
        if int == 10 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            LocateSpoonGeneration.main(target=False,graph=False)
            break
        elif int == 10 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break        
                        
        
        if int == 11 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            StirSpoonGeneration.main(target=False,graph=False)
            break
        elif int == 11 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break   
                
        if int == 12 and plan == True:
            # Used to align joints rotaion from moveit to actual robot
            JOINTS = move_grouparm.get_current_joint_values()
            JOINTS = np.array([JOINTS])
            ## For Uni Cobot ##
            JOINTS = JOINTS * -1
            JOINTS[0][2] = JOINTS[0][2] * -1
            np.save("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy",JOINTS[0])
            PlaceSpoonGeneration.main(target=False,graph=False)
            break
        elif int == 12 and plan == False:
            while (True):
                Goal[5] -= 0.339
                if Goal[5] < -3.14:
                    Goal [5]= 3.14
                go()
                print(plan)
                if plan == True:
                    break   
                
if __name__ == '__main__':
    plan(0.1,0,0.5,-1.57,0,0,0)
    
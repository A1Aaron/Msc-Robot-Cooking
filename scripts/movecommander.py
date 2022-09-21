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



move_grouparm.set_planning_time(5)
move_grouparm.set_goal_orientation_tolerance(0.01)
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
    
    print("============Initial========== Printing robot state")
    print(move_grouparm.get_current_pose())
    print("")
    get_Rotation(move_grouparm.get_current_pose())
    # Goal = input("Enter goal in x,y,z,rx,ry,rz format").split(',')
    Goal = input("Enter goal in x,y format").split(',')
    Goal.append(0.02)
    Goal.append(-1.57)
    Goal.append(0)
    Goal.append(0)
    # Goal[2]=0.13
    # Goal[3]=-1.57
    # Goal[4]=0
    # Goal[5]=0
    goal = geometry_msgs.msg.Pose()
    
    if np.size(Goal)>3:
        goal.orientation.x, goal.orientation.y, goal.orientation.z, goal.orientation.w = get_rotation(float(Goal[3]),float(Goal[4]),float(Goal[5]))
        goal.position.x = float(Goal[0])
        goal.position.y = float(Goal[1])
        goal.position.z = float(Goal[2])
        move_grouparm.set_pose_target(goal)
        plan = move_grouparm.go(wait=True)
        move_grouparm.stop()
        move_grouparm.clear_pose_targets()
        t = move_grouparm.get_current_joint_values()
        t = np.array(t)
        print(t*180/np.pi)
        np.save("/home/aaron/catkin_ws/src/mycobot/scripts/angleGoal.npy",move_grouparm.get_current_joint_values())

        rospy.sleep(1)
    else:
        goal.position.x = float(Goal[0])
        goal.position.y = float(Goal[1])
        goal.position.z = float(Goal[2])
        move_grouparm.set_pose_target(goal)
        plan = move_grouparm.go(wait=True)
        move_grouparm.stop()
        move_grouparm.clear_pose_targets()
        print(move_grouparm.get_current_joint_values())
        np.save("/home/aaron/catkin_ws/src/mycobot/scripts/angleGoal.npy",move_grouparm.get_current_joint_values())
        rospy.sleep(1)



rospy.spin()



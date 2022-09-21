from colorsys import rgb_to_hls
from re import I
import sys
from tkinter.tix import Tree
import rospy
import moveit_commander
import moveit_msgs.msg
import numpy as np
from numpy import load
from math import pi, tau, dist, fabs, cos
from moveit_commander.conversions import pose_to_list
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from scipy.spatial.transform import Rotation as R
import cv2


R_G2B = []
R_C2T = []
T_G2B = []
T_C2T = []


    
    
    

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
        return roll,pitch,yaw
    
    print("============Initial Position======================= Printing robot state")
    print(move_grouparm.get_current_pose())
    print("")
    get_Rotation(move_grouparm.get_current_pose()
                 )
    
    c2t = np.load('C2T.npy')
    t2g = np.load('T2G.npy')
    
  
       
    
    rx,ry,rz = get_Rotation(move_grouparm.get_current_pose())
    T = move_grouparm.get_current_pose()
    rgrip = R.from_euler('xyz',[[rx,ry,rz]],degrees=False)
    rgrip = rgrip.as_matrix()
    rgrip = rgrip[0]
    tgrip = np.array([[T.pose.position.x],[T.pose.position.y],[T.pose.position.z]])
    
    
  
    
    # Changes B2G to G2B
    rgrip = rgrip.T 
    tgrip = np.matmul(-rgrip,tgrip)
        
    
    
    g2b = np.concatenate([rgrip,tgrip],axis = 1)
    lastrow = np.array([[0,0,0,1]])
    g2b = np.concatenate([g2b,lastrow],axis = 0)
    
    base = np.matmul(np.matmul(c2t,t2g),g2b)
    print(base)
# rospy.spin()



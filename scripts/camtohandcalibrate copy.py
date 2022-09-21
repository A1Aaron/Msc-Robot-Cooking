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
    
    jointTarget = np.load('jointarray.npy')*np.pi/180
    camposeT = np.load('charucoposeT.npy')
    camposeR = np.load('charucoposeR.npy')
    for x in range(int(np.size(jointTarget)/6)):
        move_grouparm.set_joint_value_target(jointTarget[x])
        plan = move_grouparm.go(wait=True)
        print("PLAN")
        print(plan) 
        rospy.sleep(1)
        print("ROBOT POS {}".format(x+1) )
        print(move_grouparm.get_current_pose())
        rx,ry,rz = get_Rotation(move_grouparm.get_current_pose())
        T = move_grouparm.get_current_pose()
        print("")
        
        rcam = R.from_euler('xyz',camposeR[x].T,degrees=False)
        rcam = rcam.as_matrix()
        rcam = rcam[0]
        tcam = camposeT[x]
        print ("CAMERA")
        print(rcam)
        print(tcam)
        print("") 
        
        rgrip = R.from_euler('xyz',[[rx,ry,rz]],degrees=False)
        rgrip = rgrip.as_matrix()
        rgrip = rgrip[0]
        tgrip = np.array([[T.pose.position.x],[T.pose.position.y],[T.pose.position.z]])
        tgrip = tgrip*1000
        print("ROBOT")
        print (rgrip)
        print(tgrip)
        print("")
        if plan == True:
            
            # Changes B2G to G2B
            rgrip = rgrip.T 
            tgrip = np.matmul(-rgrip,tgrip)
             
             
            R_G2B.append(rgrip)
            T_G2B.append(tgrip)

            R_C2T.append(rcam)
            T_C2T.append(tcam)

        move_grouparm.stop()
        move_grouparm.clear_pose_targets()
    
    
    rcalib, tcalib = cv2.calibrateHandEye(R_G2B,T_G2B,R_C2T,T_C2T)
    
    print(np.shape(R_G2B)[0])
    print(rcalib)
    print(tcalib)
    calib = np.concatenate([rcalib,tcalib],axis = 1)
    print(calib)
    np.save("calib",calib)
    rospy.signal_shutdown("end")

# rospy.spin()



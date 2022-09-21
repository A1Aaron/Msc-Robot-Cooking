from ntpath import join
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import numpy as np
from tf.transformations import euler_from_quaternion, quaternion_from_euler

def finalpose():
        
    Goal = np.zeros(6)
    FinalPoses = []
    Y = 0


        

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
            orientation_list = [orientation_q.x,orientation_q.y, orientation_q.z, orientation_q.w]
            (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
            print(roll,pitch,yaw)
            return roll,pitch,yaw
        
        pickTeaCup = np.load('/home/aaron/catkin_ws/src/mycobot/data/PICK_CUP_FinalJoints.npy')*np.pi/180
        placeTeaCup = np.load('/home/aaron/catkin_ws/src/mycobot/data/PLACE_CUP_FinalJoints.npy')*np.pi/180
        pickTeaBag = np.load('/home/aaron/catkin_ws/src/mycobot/data/PICK_TEA_FinalJoints.npy')*np.pi/180
        placeTeaBag = np.load('/home/aaron/catkin_ws/src/mycobot/data/PLACE_TEA_FinalJoints.npy')*np.pi/180#
        pickWaterCup = np.load('/home/aaron/catkin_ws/src/mycobot/data/PICK_H20_FinalJoints.npy')*np.pi/180
        locateWaterCup = np.load('/home/aaron/catkin_ws/src/mycobot/data/LOCATE_H20_FinalJoints.npy')*np.pi/180
        pourWaterCup = np.load('/home/aaron/catkin_ws/src/mycobot/data/POUR_H20_FinalJoints.npy')*np.pi/180
        placeWaterCup = np.load('/home/aaron/catkin_ws/src/mycobot/data/PLACE_H20_FinalJoints.npy')*np.pi/180
        pickSpoon = np.load('/home/aaron/catkin_ws/src/mycobot/data/PICK_SPOON_FinalJoints.npy')*np.pi/180
        locateSpoon = np.load('/home/aaron/catkin_ws/src/mycobot/data/LOCATE_SPOON_FinalJoints.npy')*np.pi/180
        stirSpoon = np.load('/home/aaron/catkin_ws/src/mycobot/data/STIR_SPOON_FinalJoints.npy')*np.pi/180
        placeSpoon = np.load('/home/aaron/catkin_ws/src/mycobot/data/PLACE_SPOON_FinalJoints.npy')*np.pi/180
        
        poses = [pickTeaCup,placeTeaCup,pickTeaBag,placeTeaBag,pickWaterCup,locateWaterCup,pourWaterCup,placeWaterCup,pickSpoon,locateSpoon,stirSpoon,placeSpoon]
        for X in zip(poses):
            Y +=1
            print(X[0]*180/np.pi)
            if X[0][4] < -2.87:
                X[0][4] = -2.87
            X[0][0] *= -1
            X[0][1] *= -1
            X[0][3] *= -1
            X[0][4] *= -1
            X[0][5] *= -1
            move_grouparm.set_joint_value_target(X[0])
            plan = move_grouparm.go(wait=True)
            if plan == True:
                print("Getting Final Pose")
            else:
                print("Could not get Pose")
                
            msg = move_grouparm.get_current_pose()
            rx,ry,rz = get_Rotation(msg)
            x = msg.pose.position.x
            y = msg.pose.position.y
            z = msg.pose.position.z
            move_grouparm.stop()
            move_grouparm.clear_pose_targets()
            np.save('/home/aaron/catkin_ws/src/mycobot/data/pose'+str(Y),np.array([x,y,z,rx,ry,rz]))
            print("Saved Final Pose")
            # rospy.signal_shutdown("END")      
        
        break
    
    return rx,ry,rz


    
    

if __name__ == '__main__':
    finalpose()
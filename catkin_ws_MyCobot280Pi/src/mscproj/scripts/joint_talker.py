import rospy
from mycobot.msg import joint
from pymycobot import MyCobot, PI_BAUD, PI_PORT

angles = []


def talker():
    pub = rospy.Publisher('cobot_joints',joint,queue_size=20)
    rospy.loginfo("[INFO] Starting the jointtalker node")
    rospy.init_node('mycobot_joints',anonymous=True)
    rate = rospy.Rate(60)
    
    while not rospy.is_shutdown():
        angles = mc.get_angles()
        gripper_state = mc.get_gripper_value()
        if gripper_state != -1:
            angles.append(gripper_state)
        pub.publish(angles)
        rate.sleep()
        
        
    








if __name__ == '__main__':
    
    mc = MyCobot(PI_PORT,PI_BAUD)
    talker()
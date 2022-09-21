#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from pymycobot import MyCobot, PI_BAUD, PI_PORT
import numpy as np
from mycobot.msg import joint

def main():
    mc = MyCobot(PI_PORT,PI_BAUD)
    rospy.init_node("MyCobot",anonymous=True)
    pubangles = rospy.Publisher("my_cobotjoints",joint,queue_size=10)
    rate = rospy.Rate(5)
    Angles = [None]*6
    

    while not rospy.is_shutdown():
        rospy.loginfo("[INFO] Publishing my cobot joint angles") 
        angles = mc.get_angles()
        print(Angles)
        if np.size(angles) == 6:
            Angles[0] = angles[0]
            Angles[1] = angles[1]
            Angles[2] = angles[2]
            Angles[3] = angles[3]
            Angles[4] = angles[4]
            Angles[5] = angles[5]
            pubangles.publish(Angles)






if __name__ == "__main__":
    main()
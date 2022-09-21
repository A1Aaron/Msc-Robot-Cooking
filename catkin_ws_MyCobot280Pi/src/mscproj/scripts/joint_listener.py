#!/usr/bin/python3
import rospy
from sensor_msgs.msg import JointState
from pymycobot import MyCobot, PI_BAUD, PI_PORT
import math
import time
global x
x=0

    
def sendangles(position):
    global x
    def map_range(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    grip = map_range(position[0],0,1.57931,0,100)
    
    mc.send_radians([-position[6], -position[7],position[8],-position[9], -position[10],-position[11]], 50)
    if x == 10:
        
        if grip <= 25:
            mc.set_gripper_state(1,50) 
            x = 0
        
        elif grip >=75:
            mc.set_gripper_state(0,50) 
            x = 0
        else:
            x=0 
    x+=1  
    

def callback(jointstate):
    # Print out what was heard to terminal 
    rospy.loginfo("Joint states heard were: [{}]".format (jointstate.position))
    sendangles(jointstate.position)

    
def listener():
    # Creates a node called jointlistener and gives it a unique name for every instance
    rospy.loginfo("[INFO] Starting the jointlistener node")
    rospy.init_node('jointlistener',anonymous=True)
    # Subscribes to topic called joint_state published by rviz
    rospy.Subscriber("/joint_states",JointState,callback)
    # Keeps python code from exiting until the node is stopped
    rospy.spin()
    
if __name__ == '__main__':
    
    mc = MyCobot(PI_PORT,PI_BAUD)
    listener()
    

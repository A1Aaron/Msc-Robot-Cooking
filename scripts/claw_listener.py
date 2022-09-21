#!/usr/bin/env python3
from email.mime import message

from cv2 import meanShift
import rospy
from sensor_msgs.msg import JointState
from pymycobot import MyCobot, PI_BAUD, PI_PORT
import math
import time
import bluetooth
import sys


message_num = 0
previous = 0

def sendangles(position):
    global message_num
    global previous
    
    print(message_num)
    
    if (message_num > 15):
        if position[0] < previous:
            
            sock.send("0")
            message_num = 0

            
        elif position[0] > previous:
            sock.send("1")
            message_num = 0
        
    previous = position[0]
    
    
    

def callback(jointstate):
    # Print out what was heard to terminal 
    # rospy.loginfo("Joint states heard were: [{}]".format (jointstate.position))
    sendangles(jointstate.position)
    global message_num
    message_num += 1

    
def listener():
    # Creates a node called jointlistener and gives it a unique name for every instance
    rospy.loginfo("[INFO] Starting the jointlistener node")
    rospy.init_node('clawlistener',anonymous=True)
    # Subscribes to topic called joint_state published by rviz
    rospy.Subscriber("/joint_states",JointState,callback)
    # Keeps python code from exiting until the node is stopped
    rospy.spin()
    
if __name__ == '__main__':
    
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print ("Found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices :
        print("    %s - %s" %(addr, name))
    

    addr = "E8:9F:6D:27:74:76"

    service_matches = bluetooth.find_service(address=addr)

    if len(service_matches) == 0:
        print("Couldn't find the ESP32")
        sys.exit(0)

    first_match = service_matches[0]
    port = first_match["port"]
    name = first_match["name"]
    host = first_match["host"]

    print("Connecting to \"{}\" on {}".format(name, host))

    # Create the client socket
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))
    listener()
   

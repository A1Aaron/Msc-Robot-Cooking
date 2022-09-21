import rospy
from std_msgs.msg import Float32MultiArray

def callback(joint):
    rospy.loginfo("MC Joint values are: {}".format(joint))



def main():
    rospy.loginfo("[INFO] Reading my cobot joint angles")
    rospy.init_node('dmp_joint_listener',anonymous=True)
    rospy.Subscriber("my_cobotjoints",Float32MultiArray,callback)
    rospy.spin()
    




if __name__ == "__main__":
    main()
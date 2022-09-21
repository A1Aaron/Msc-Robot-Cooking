import rospy 
from tf2_msgs.msg import TFMessage
import tf2_ros as tf
from std_msgs.msg import Float64MultiArray


    
def main():
    rospy.loginfo("[INFO] Starting the poselistener node")
    rospy.init_node('poselistener',anonymous=True)
    pub = rospy.Publisher('/pickPointframe',Float64MultiArray,queue_size=10)
    rate = rospy.Rate(10)
    
    tfBuffer = tf.Buffer()
    listener = tf.TransformListener(tfBuffer)
    
    while not rospy.is_shutdown():
        try:
            trans= tfBuffer.lookup_transform("base_link","Pickpoint", rospy.Time())
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
        # print (trans)
        
        msg = Float64MultiArray()
        msg.data = [trans.transform.translation.x, trans.transform.translation.y, trans.transform.translation.z, 
                    trans.transform.rotation.x, trans.transform.rotation.y, trans.transform.rotation.z,trans.transform.rotation.w]
        pub.publish(msg)
        rate.sleep()
    
if __name__ == '__main__':
    
    main()
    
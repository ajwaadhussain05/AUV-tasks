#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    result = data.data * 10  #multiplies the received number by 10
    rospy.loginfo("Subscriber 1: %d", result)  #log the result
    pub.publish(result)  #to publish the result to a new topic

rospy.init_node('subscriber_1', anonymous=True)
pub = rospy.Publisher('multiplied_numbers', Int32, queue_size=10)  #publisher for multiplied numbers
rospy.Subscriber('numbers', Int32, callback)  #subscriber for original numbers

rospy.spin()  #this is to keep the node running

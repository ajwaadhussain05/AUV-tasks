#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    result = data.data + 5  #adds 5 to the received number
    rospy.loginfo("Subscriber 2: %d", result)  #log the final result

rospy.init_node('subscriber_2', anonymous=True)
rospy.Subscriber('multiplied_numbers', Int32, callback)  #subscriber for multiplied numbers

rospy.spin()  #this is done to keep the node running

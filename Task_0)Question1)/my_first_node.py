#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    # This fxn is called if a message is received on the 'chat_topic'
    rospy.loginfo("Jolyne: %s", data.data)
    response = "Joestar: " + data.data  # Joestar responds
    pub.publish(response)  # this is to publish the response


rospy.init_node('chat_node', anonymous=True)
pub = rospy.Publisher('chat_topic', String, queue_size=10)  #publisher for chat messages
rospy.Subscriber('chat_topic', String, callback)  #subscriber for chat messages

rospy.spin()  #this is done to keep the node running

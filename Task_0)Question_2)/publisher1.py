#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('numbers', Int32, queue_size=10)  #puublisher for numbers
    rospy.init_node('number_publisher', anonymous=True)
    rate = rospy.Rate(1)
    num = 0
    while not rospy.is_shutdown():
        num += 2  #increment by 2
        rospy.loginfo(num)  #log the number
        pub.publish(num)  #to publish the number
        rate.sleep()  #sleep for a while

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

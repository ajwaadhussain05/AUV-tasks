#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('commands', String, queue_size=10)  #publisher for commands
    rospy.init_node('command_publisher', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        command = input("Enter command (forward/turn left): ")  #user input for commands
        pub.publish(command)  #to publish the command
        rate.sleep()  #sleep for a while

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

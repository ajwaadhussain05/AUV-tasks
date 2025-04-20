#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray, String

#to initialize position and direction
x = 0.0 
y = 0.0  
direction = "N"  #initializing facing direction

def move_bot(command):
    global x, y, direction
    if command == "forward":
        if direction == "N":
            y += 1
        elif direction == "S":
            y -= 1
        elif direction == "E":
            x += 1
        elif direction == "W":
            x -= 1
    elif command == "turn left":
        if direction == "N":
            direction = "W"
        elif direction == "W":
            direction = "S"
        elif direction == "S":
            direction = "E"
        elif direction == "E":
            direction = "N"
    
    #publish the updated position and direction
    position = Float32MultiArray()
    position.data = [x, y]  #position as [x, y]
    pub_position.publish(position)  #publish position

    pub_direction.publish(direction)  #publish direction

def callback(data):
    move_bot(data.data)  #call move_bot with the received command

rospy.init_node('bot_subscriber', anonymous=True)
pub_position = rospy.Publisher('bot_position', Float32MultiArray, queue_size=10)  #publisher for bot position
pub_direction = rospy.Publisher('bot_direction', String, queue_size=10)  # publisher for bot direction
rospy.Subscriber('commands', String, callback)  #subscriber for commands

rospy.spin()  #to keep the node running

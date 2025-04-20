#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class EdgeImageSubscriber:
    def __init__(self):
        rospy.init_node('edge_image_subscriber', anonymous=True)
        
        #creatinng a CvBridge object
        self.bridge = CvBridge()
        
        #subscribe to the edge image topic
        self.image_sub = rospy.Subscriber('camera/edge_image', Image, self.callback)

    def callback(self, data):
        #convertinng the ROS Image message to OpenCV format
        edge_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="mono8")
        
        #displaying the edge image
        cv2.imshow("Edge Image", edge_image)
        cv2.waitKey(1)

if __name__ == '__main__':
    try:
        edge_image_subscriber = EdgeImageSubscriber()
        rospy.spin()  #to keep the node running
    except rospy.ROSInterruptException:
        pass

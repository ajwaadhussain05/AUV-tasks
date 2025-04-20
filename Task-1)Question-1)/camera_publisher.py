#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraEdgePublisher:
    def __init__(self):
        rospy.init_node('camera_edge_publisher', anonymous=True)
        
        #create a publisher for the image topic
        self.image_pub = rospy.Publisher('camera/edge_image', Image, queue_size=10)
        
        #create a CvBridge object to convert ROS images to OpenCV format
        self.bridge = CvBridge()
        
        #start capturing video from the camera
        self.cap = cv2.VideoCapture(0)  # 0 is the default camera
        
        #checking if the camera opened successfully
        if not self.cap.isOpened():
            rospy.logerr("Could not open video device")
            exit()

    def run(self):
        while not rospy.is_shutdown():
            #capturinng it frame-by-frame
            ret, frame = self.cap.read()
            if not ret:
                rospy.logerr("Failed to capture image")
                break
            
            #convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            #apply Canny edge detection
            edges = cv2.Canny(gray_frame, 100, 200)
            
            #convert the edges image to a ROS Image message
            edge_image_msg = self.bridge.cv2_to_imgmsg(edges, encoding="mono8")
            
            #publish the edge image
            self.image_pub.publish(edge_image_msg)
            
            #to display the original frame
            cv2.imshow("Camera Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        #release the camera and close windows
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        camera_edge_publisher = CameraEdgePublisher()
        camera_edge_publisher.run()
    except rospy.ROSInterruptException:
        pass

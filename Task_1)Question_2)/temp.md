# Edge Detection Pipeline

## Overview
This project builds on the camera output by applying edge detection to the images and publishing the processed images to a ROS topic.

## My Approach
1. **Set Up Subscriber Node**: I created a ROS node called `edge_image_subscriber` to listen for images.
2. **Receive Images**: Subscribed to the `camera/edge_image` topic to get the images.
3. **Process Images**: Applied edge detection using OpenCV and displayed the results.

## Challenges Faced
- **Time Management**: The installation of Ubuntu and ROS took a lot of time, which delayed my progress on this project.
- **Image Conversion**: I had some initial confusion with converting ROS images to OpenCV format, but I managed to resolve it.

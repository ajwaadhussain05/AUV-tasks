# Chat Package Approach

## Approach
In this package, my goal was to enable two users, Jolyne and Joestar, to chat with each other using a single ROS node and topic. I aimed to create a simple yet effective communication system that would allow for back-and-forth messaging.

## Methods
1. **ROS Node Initialization**: 
   - I initialized a ROS node.
   - I created a publisher to send messages.
   - I set up a subscriber to receive messages.

2. **Callback Function**: 
   - I implemented a callback function that processes incoming messages and generates a response.
   - The response is published back to the same topic, allowing for a straightforward chat interaction.

3. **Logging**: 
   - I used `rospy.loginfo` to log messages for debugging and monitoring purposes.

## Problems Faced
- **Message Handling**: I initially faced challenges with message formatting and ensuring that responses were correctly structured.

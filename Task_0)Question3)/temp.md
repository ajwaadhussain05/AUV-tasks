# Bot Movement Package Approach

## Approach
The objective of this package is to allow a user to send commands to control a bot's movement in a Cartesian plane. The bot's position and direction are updated based on the commands received.

## Methods
1. **Command Publisher**: 
   - Created a publisher node that takes user input for commands (e.g., "forward", "turn left") and publishes them to the `commands` topic.

2. **Bot Subscriber**: 
   - Implemented a subscriber that listens to the `commands` topic.
   - Maintained the bot's state (position and direction) using global variables initialized at the start of the node.
   - Updated the bot's position based on the received commands and published the position as a `Float32MultiArray` and the direction as a `String`.

3. **Logging**: 
   - Used `rospy.loginfo` to log the bot's position and direction for monitoring.

## Problems Faced
- **State Management**: Managing the bot's state (position and direction) required careful handling of global variables.
- **User  Input**: Handling user input in a non-blocking way was challenging, as it required the node to remain responsive while waiting for commands.
- **Testing Movement**: Testing the bot's movement and ensuring that the commands were correctly interpreted required multiple iterations and adjustments.

# Publisher and Subscriber Package Approach

## Approach
This package consists of a publisher that sends multiples of 2 and two subscribers that process the data. The first subscriber multiplies the received number by 10, and the second subscriber adds 5 to the result.

## Methods
1. **Publisher Node**: 
   - Created a publisher node that publishes multiples of 2 to the `numbers` topic.
   - Used it to set up the publisher.

2. **First Subscriber**: 
   - Implemented a subscriber that listens to the `numbers` topic.
   - Multiplied the received number by 10 and published the result to a new topic `multiplied_numbers`.

3. **Second Subscriber**: 
   - Created another subscriber that listens to the `multiplied_numbers` topic.
   - Added 5 to the received number and logged the final result.

## Problems Faced
- **Data Flow**: Ensuring that the data flowed correctly between the publisher and subscribers required careful management of topics.
- **Debugging**: Debugging the flow of data was challenging, especially when trying to ensure that the correct values were being published and received.

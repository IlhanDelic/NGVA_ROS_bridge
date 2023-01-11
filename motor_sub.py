#
# source code: https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html
# edited by ilhan delic
# email: ilhandelic98@outlook.com
#
import rclpy
from rclpy.node import Node #import Node so my class can inherit ros2 functions
from std_msgs.msg import String  #import message to send string messages


class MotorSubNode(Node):  #create class

    def __init__(self): 
        super().__init__('motor_sub')   #constructor of the upperclass with the node name thats going to be used in the graph
        # create subscriber (messageType, Topic name, what function to execute, buffer)
        self.subscription = self.create_subscription(String, 'ngva', self.listener_callback, 10) 
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg): #create function to print the messages send to Topic
        self.get_logger().info('I heard: "%s"' % msg.data) #print Data send on Topic


def main(args=None): #create main function
    rclpy.init(args=args) # initialise ros2 communications
    node = MotorSubNode() #creating the node with additional parameters
   
    rclpy.spin(node) #makes the code in the node loop

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node() # destroy node
    rclpy.shutdown() # shutdown ros2 communications


if __name__ == '__main__':
    main()
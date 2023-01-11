#
# source code: https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html
# edited by ilhan delic
# email: ilhandelic98@outlook.com
#
import rclpy
from rclpy.node import Node #import Node so my class can inherit ros2 functions
from std_msgs.msg import String #import message to send string messages


class MotorPubNode(Node): #create class

    def __init__(self):
        super().__init__('motor_pub') #constructor of the upperclass with the node name thats going to be used in the graph
        self.publisher_ = self.create_publisher(String, 'ngva', 10) #create publisher with(messageType, Topic name, buffer)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback) #create a timer that calls the function ever second
        self.i = 0 # set the counter to 0

    def timer_callback(self): #create function 
        msg = String() # message type is String
        msg.data = 'De motor is gestart: %d' % self.i #data send in the message
        self.publisher_.publish(msg) # publish message
        self.get_logger().info('Publishing: "%s"' % msg.data) # print send message
        self.i += 1 # add to the counter


def main(args=None): #create main function
    rclpy.init(args=args) # initialise ros2 communications
    node = MotorPubNode() #creating the node with additional parameters 

    rclpy.spin(node) #makes the code in the node loop

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node() # destroy node
    rclpy.shutdown() # shutdown ros2 communications


if __name__ == '__main__': #calling main function when you want to direcly call the function
    main()
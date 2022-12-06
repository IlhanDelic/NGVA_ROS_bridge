#!/usr/bin/env python3
import rclpy
from rclpy.node import Node #import Node so my class can inherit ros2 functions


class MyNode(Node): #create class

    def __init__(self): #create constructor
        super().__init__("first_node") #constructor of the upperclass with the node name thats going to be used in the graph
        self.get_logger().info("hello from ROS2") #self gets func form node class, logger is the way to write in ros2

def main(args=None):     #create main function 
    rclpy.init(args=args)# initialise ros2 communications
    #create node here by object oriented programming
    node = MyNode() #creating the node with additional parameters 
    rclpy.spin(node)# loops the code from node and can be terminated in terminal with ctrl + c
    rclpy.shutdown()# shutdown ros2 communications

if __name__=='__main__': #calling main function when you want to direcly call the function
    main()
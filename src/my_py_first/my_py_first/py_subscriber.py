#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubNode(Node):
    def __init__(self):
        super().__init__("Sub_Py")
        self.get_logger().info("Created Sub")
        self.__sub = self.create_subscription(String, "radio", self.on_recieve, 10)


    def on_recieve(self, msg):
        self.get_logger().info(f"Got info as {msg.data}")

def main(args=None):
    rclpy.init(args=args)

    node = SubNode()
    rclpy.spin(node)

    rclpy.shutdown()
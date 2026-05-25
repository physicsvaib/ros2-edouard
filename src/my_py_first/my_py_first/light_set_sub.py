#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStates

class LedStateSub(Node):
    def __init__(self):
        super().__init__("LedStateSub")
        self.sub = self.create_subscription(LedStates, "led_states", self.sub_callback, 10)
        self.get_logger().info("Led State Sub activated")

    def sub_callback(self, data):
        self.get_logger().info(f"Found {data}")

def main(args=None):
    rclpy.init(args=args)

    node = LedStateSub()

    rclpy.spin(node)
    rclpy.shutdown()



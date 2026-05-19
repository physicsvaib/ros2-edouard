#!/usr/bin/env python3

import rlcompleter
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

from example_interfaces.srv import SetBool

class NumberCounter(Node):
    def __init__(self):
        super().__init__("Number_Counter")
        self._sub = self.create_subscription(Int64, "number", self.sub_callback, 10)
        self._pub = self.create_publisher(Int64, "number_counter", 10)
        self.get_logger().info("Started Number Counter")
        self._counter = 0
        self.service = self.create_service(SetBool, "reset_counter", self.reset_counter_value)

    def reset_counter_value(self, req, res):
        if req.data:
            self._counter = 0
            res.success = True
            res.message = "Reset value done"
        else:
            res.success = False
            res.message = "You fired with wrong value"
        return res

    def sub_callback(self, msg):
        self.get_logger().info(f"Recieved {msg}")
        self._counter += msg.data
        
        new_count = Int64()
        new_count.data = self._counter
        self._pub.publish(new_count)

def main(args=None):
    rclpy.init(args=args)

    node = NumberCounter() 
    rclpy.spin(node)

    rclpy.shutdown()

    
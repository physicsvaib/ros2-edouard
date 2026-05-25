#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import BatteryStatus

class BatteryNode(Node):
    def __init__(self):
        super().__init__("BatteryNode")

        self.get_logger().info("Created a battery Node")
        self.client = self.create_client(BatteryStatus, "battery_status")
        self.call_timer = self.create_timer(5, self.timer_callback)
        self.is_battery_empty = False


    def make_request_for_status(self, led_number, led_state):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("No Service for battery_status")
        
        req = BatteryStatus.Request()
        req.led_number = led_number
        req.led_state = led_state

        future = self.client.call_async(req)
        future.add_done_callback(self.future_callback)

    def future_callback(self, future):
        res = future.result()
        self.get_logger().info(f"Status was {res}")

    def timer_callback(self):
        self.is_battery_empty = not self.is_battery_empty
        self.make_request_for_status(2, not self.is_battery_empty)
        

def main(args=None):
    rclpy.init(args=args)

    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()



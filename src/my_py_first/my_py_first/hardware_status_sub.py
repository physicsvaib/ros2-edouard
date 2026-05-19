#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus


class HardwareStatusSub(Node):
    def __init__(self):
        super().__init__("Hardware_Status_Sub")
        self.sub = self.create_subscription(HardwareStatus, "hardware", self.sub_callback, 10)

    def sub_callback(self, msg: HardwareStatus):
        self.get_logger().info(f"{msg.temprature} {msg.are_machines_running} {msg.debug_message}")

def main(args=None):
    rclpy.init(args=args)

    node = HardwareStatusSub()

    rclpy.spin(node)
    rclpy.shutdown()
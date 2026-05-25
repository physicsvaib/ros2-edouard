#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ComputeRectangleArea

class RectangleAreaClient(Node):
    def __init__(self):
        super().__init__("RectangleAreaClient")
        self.client = self.create_client(ComputeRectangleArea, "rectangle_area")
        self.get_logger().info("Started the client for area")

    def calc_area(self, width, height):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("Hey no service for the area calc")
        
        req = ComputeRectangleArea.Request()
        req.height = height
        req.width = width

        future = self.client.call_async(req)
        future.add_done_callback(self.future_callback)

    def future_callback(self, future):
        res = future.result()
        self.get_logger().info(f"result is {res}")

def main(args=None):
    rclpy.init(args=args)

    node = RectangleAreaClient()
    node.calc_area(5.0,15.0)

    rclpy.spin(node)
    rclpy.shutdown()
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ComputeRectangleArea


class RectangleAreaService(Node):
    def __init__(self):
        super().__init__("RectangleAreaService")
        self.srv = self.create_service(ComputeRectangleArea, "rectangle_area", self.compute_callback)
        self.get_logger().info("Started Rectangle Area Compute Service")

    def compute_callback(self, req, res):
        res.area = req.width * req.height
        self.get_logger().info(f"{req.width} * {req.height} = {res.area}")
        return res

def main(args=None):
    rclpy.init(args=args)

    node = RectangleAreaService()

    rclpy.spin(node)
    rclpy.shutdown()
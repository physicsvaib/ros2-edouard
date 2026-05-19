#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddServiceNode(Node):
    def __init__(self):
        super().__init__("Add_Service")
        self.service = self.create_service(AddTwoInts, "add_ints", self.adder)

        self.get_logger().info("Started Add Service")

    def adder(self, req, res):
        res.sum = req.a + req.b
        self.get_logger().info(f"{req.a} + {req.b} = {res.sum}")
        return res



def main(args=None):
    rclpy.init(args=args)

    node = AddServiceNode()
    rclpy.spin(node)


    rclpy.shutdown()
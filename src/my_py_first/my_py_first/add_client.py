#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class ClientNode(Node):
    def __init__(self):
        super().__init__("Client_Adder")
        self.get_logger().info("Started Client Node for add")
        self.client = self.create_client(AddTwoInts, "add_ints")
    
    def make_calc(self, a, b):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("Hey no service mate")
        req = AddTwoInts.Request()
        req.a = a
        req.b = b

        future = self.client.call_async(req)
        future.add_done_callback(self.calc_callback)

    def calc_callback(self, future):
        res = future.result()
        self.get_logger().info(f"Hey {res}")



def main(args=None):
    rclpy.init(args=args)

    node = ClientNode()
    node.make_calc(5,5)

    rclpy.spin(node)
    rclpy.shutdown()

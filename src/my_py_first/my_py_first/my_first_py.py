#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class FirstNode(Node):
    def __init__(self) -> None:
        super().__init__("First")
        self.get_logger().info("Started Firster")
        self.create_timer(2, self.printer)

    def printer(self):
        self.get_logger().info("Printing from outside")
    


def main(args=None):
    rclpy.init(args=args)

    node = FirstNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
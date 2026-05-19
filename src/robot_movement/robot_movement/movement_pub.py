#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class MovmentPub(Node):
    def __init__(self):
        super().__init__("Movement_Pub")
        self.publisher = self.create_publisher(String, "movement_data", 10)
        self.timer = self.create_timer(2, self.timer_callback)
        self.get_logger().info("Movement Pub Init")

    def timer_callback(self):
        msg = String()
        val = random.randrange(0, 400)
        if val % 3 == 0:
            msg.data = "Move Forward"
        elif val % 3 == 1:
            msg.data = "Turn Left"
        elif val % 3 == 2:
            msg.data = "Turn Right"

        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    node = MovmentPub()
    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

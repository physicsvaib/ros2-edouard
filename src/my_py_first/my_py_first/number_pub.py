#!/usr/bin/env pyhton3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class NumberPub(Node):
    def __init__(self):
        super().__init__("Number_Pub")
        self.declare_parameter("MsgValue", 2)
        self.declare_parameter("TimerValue", 2.0)

        self.get_logger().info("Number Publisher Spawned")
        self._pub = self.create_publisher(Int64, "number", 10)
        self._timer = self.create_timer(self.get_parameter("TimerValue").value, self.timer_callback)

    def timer_callback(self):
        msg = Int64()
        msg.data = self.get_parameter("MsgValue").value
        self._pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = NumberPub()
    rclpy.spin(node)
    
    rclpy.shutdown()
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PubNode(Node):
    def __init__(self):
        super().__init__("Pub_Node_Py")
        self.get_logger().info("Publisher Started Py")
        self.__pub = self.create_publisher(String, "radio", 10)
        self.__pub_timer = self.create_timer(2, self.publisher)
        self.declare_parameter("RadioName", "Awesome Studio")


    def publisher(self):
        msg = String()
        msg.data = f"Hey Yo from {self.get_parameter("RadioName").value}"
        self.__pub.publish(msg)
    

def main(args=None):
    rclpy.init(args=args)

    node = PubNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
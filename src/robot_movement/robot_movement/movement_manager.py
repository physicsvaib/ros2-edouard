#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MovementManager(Node):
    def __init__(self):
        super().__init__("Movement_Manager")
        self.sub = self.create_subscription(String, "movement_data", self.listen_sub_callback, 10)
        self.pub = self.create_publisher(String, "movement_state", 10)
        self.state = 'Idle'
        self.get_logger().info(f"Init MovementManager, current state {self.state}")

    def listen_sub_callback(self, msg):
        if(msg.data == "Activate"):
            self.state = 'Start'
        elif (msg.data == "Deactivate"):
            self.state = 'IDLE'

        msg = String()
        msg.data = self.state
        self.pub.publish(msg)


        self.get_logger().info(f"got data back {msg.data} now the state is {self.state}")



def main(args=None):
    rclpy.init(args=args)

    node = MovementManager()
    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()
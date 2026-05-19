#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MovementSubscriber(Node):
    def __init__(self):
        super().__init__("First_Movement_Listener")
        self.subcription = self.create_subscription(
            String, "movement_data", self.listener_callback, 10
        )
        self.get_logger().info("Movement Pub Initialized")

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')
       
        match(msg.data):
            case "Move Forward":
                self.move_forward()
            case "Move Back":
                self.move_back()
            case "Turn Left":
                self.turn_left()
            case "Turn Right":
                self.turn_right()
            case "Stop":
                self.stop()
        
        

    def move_forward(self):
        self.get_logger().info("Robot is moving forward.")

    def turn_left(self):
        self.get_logger().info("Robot is turning left.")

    def turn_right(self):
        self.get_logger().info("Robot is turning right.")

    def move_back(self):
        self.get_logger().info("Robot is moving back now.")

    def stop(self):
        self.get_logger().info("Robot is resting now, STOP.")



def main(args=None):
    rclpy.init(args=args)
    node = MovementSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

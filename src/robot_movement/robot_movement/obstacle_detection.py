#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String


class ObstacleDetection(Node):
    def __init__(self):
        super().__init__("Obstacle_Detection")

        self.sub = self.create_subscription(LaserScan, "obstacle", self.obstacle_callback, 10)
        self.pub = self.create_publisher(String, "movement_data", 10)

        self.get_logger().info("Created Obstacle Detector")

    def obstacle_callback(self, obs):
        closest_dis = min(obs.ranges)
        if closest_dis < 1.0:
            self.raise_stop()

    def raise_stop(self):
        stopper = String()
        stopper.data = "Stop"
        self.pub.publish(stopper)
        self.get_logger().info("Stopping due to obs")

def main(args=None):
    rclpy.init(args=args)

    node = ObstacleDetection()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
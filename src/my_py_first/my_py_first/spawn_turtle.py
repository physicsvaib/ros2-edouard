#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random

class SpawnTurtle(Node):
    def __init__(self):
        super().__init__("SpawnTurtleNode")
        
        self.declare_parameter("DelayInSpawn", 2.0)
        self.timer_to_spawn = self.create_timer(self.get_parameter("DelayInSpawn").value, self.spawn_turtle_handler)
        self.get_logger().info("lets spawn some turtlesss")
        self.client = self.create_client(Spawn, "/spawn")

    def spawn_turtle_handler(self):
        self.get_logger().info("Should be spawning a turle like right now")
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("No client spawned for turtle spawn")

        req = Spawn.Request()
        req.x = random.uniform(0, 10)
        req.y = ramdom.uniform(0, 10)
        req.theta = random.uniform(0, 360)

        future = self.client.call_async(req)
        future.add_done_callback(self.on_turtle_spawn)
    
    def on_turtle_spawn(self, future):
        res = future.result()
        self.get_logger().info(f"result is {res}")


def main(args=None):
    rclpy.init(args=args)

    node = SpawnTurtle()

    rclpy.spin(node)
    rclpy.shutdown()

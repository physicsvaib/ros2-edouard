#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import LedStates
from my_robot_interfaces.srv import BatteryStatus

class LightSet(Node):
    def __init__(self):
        super().__init__("LightSet")
        
        self.declare_parameter("LedInitState", [False, False, False])
        self.led_states = self.get_parameter("LedInitState").value

        self.get_logger().info("Created a new light set")

        self.service = self.create_service(BatteryStatus, "battery_status", self.handle_service_req)
        self.light_state_pub = self.create_publisher(LedStates, "led_states", 10)
        self.light_state_pub_timer = self.create_timer(1, self.handle_publish_led_states)

    def handle_publish_led_states(self):
        # self.get_logger().info(f"Current States is {[i for i in self.led_states]}")
        data = LedStates()
        data.led_states = self.led_states
        self.light_state_pub.publish(data)

    def handle_service_req(self, req, res):
        if req.led_state:
            self.get_logger().info(f"We have switched the light {req.led_number} off")
        else:
            self.get_logger().info(f"We have switched the light {req.led_number} on as battery has been drained out")
        
        self.led_states[req.led_number] = not req.led_state

        res.success = True
        return res


def main(args=None):
    rclpy.init(args=args)

    node = LightSet()

    rclpy.spin(node)
    rclpy.shutdown()

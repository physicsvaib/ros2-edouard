#!/usr/bin/env python3

import rclpy
from rclpy.node import Node  
from my_robot_interfaces.msg import HardwareStatus

class HardwareStatusPub(Node):
    def __init__(self):
        super().__init__("Hardware_Status_Pub")
        self.pub = self.create_publisher(HardwareStatus, "hardware", 10)
        self.timer = self.create_timer(2, self.timer_callback)

    def timer_callback(self):
        msg = HardwareStatus()
        msg.temprature = 20.0
        msg.are_machines_running = False
        msg.debug_message = "Hey this is coming from custom interfaces..."
        self.pub.publish(msg)
    

def main(args=None):
    rclpy.init(args=args)
    
    node = HardwareStatusPub()

    rclpy.spin(node)
    rclpy.shutdown() 
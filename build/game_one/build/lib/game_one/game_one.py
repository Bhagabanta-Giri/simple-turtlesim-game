#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from turtlesim.srv import Spawn, SetPen
from geometry_msgs.msg import Twist

import math
import time


class game_one(Node):

    def __init__(self):

        super().__init__("game_one")
        self.thief_pose = None
        self.police_pose = None
        self.start_time = None
        self.game_over = False
        self.pens_cleared = False
        self.spawn_client = self.create_client(Spawn, 'spawn')
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Waiting for turtlesim spawn service...')
        
        request = Spawn.Request()
        request.x = 2.0
        request.y = 2.0
        request.theta = 0.0
        request.name = 'police'
        self.spawn_client.call_async(request)
        self.get_logger().info('Police turtle spawned! Game starting...')
        self.start_time = time.time()

        self.pen_client_thief = self.create_client(SetPen, 'turtle1/set_pen')
        self.pen_client_police = self.create_client(SetPen, 'police/set_pen')

        self.thief_sub = self.create_subscription(Pose, "turtle1/pose", self.thief_callback, 10)
        self.police_sub = self.create_subscription(Pose, "police/pose", self.police_callback, 10)
        self.police_pub = self.create_publisher(Twist, "police/cmd_vel", 10)

        self.timer = self.create_timer(0.1, self.gameloop)

    def thief_callback(self, msg):
        self.thief_pose = msg
    
    def police_callback(self, msg):
        self.police_pose = msg

    def gameloop(self):

        if not self.pens_cleared:
            if self.pen_client_thief.service_is_ready() and self.pen_client_police.service_is_ready():
                req = SetPen.Request()
                req.off = 1
                
                self.pen_client_thief.call_async(req)
                self.pen_client_police.call_async(req)
                
                self.pens_cleared = True

        if self.game_over or self.thief_pose is None or self.police_pose is None:
            return
        
        msg = Twist()
        
        dx = self.thief_pose.x - self.police_pose.x
        dy = self.thief_pose.y - self.police_pose.y

        distance = math.hypot(dx, dy)

        angle = math.atan2(dy, dx) - self.police_pose.theta
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi

        if distance <= 0.5:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.police_pub.publish(msg)

            self.game_over = True
            score = time.time() - self.start_time

            self.get_logger().info('\n' + '='*40)
            self.get_logger().info(' BUSTED! The Police caught you!')
            self.get_logger().info(f' SURVIVAL TIME (SCORE): {score:.2f} seconds')
            self.get_logger().info('='*40 + '\n')
            return
        
        elif distance >= 0.5:
            msg.linear.x = min(distance, 3.0)
            msg.angular.z = min(angle, 3.0)
        
        self.police_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = game_one()
    rclpy.spin(node)
    rclpy.shutdown()
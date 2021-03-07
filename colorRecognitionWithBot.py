import rospy
import cv2
import numpy as np
from turtleAPI import robot
from colorRecognition import ColorFinder
import PIDController


if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)

    cf = ColorFinder()
    lpid = PIDController.LinearSpeedPIDController(k_p=0.1, k_i=0.1, k_d=0, num_time_steps=5)
    apid = PIDController.AngularSpeedPIDController(k_p=0.1, k_i=0.1, k_d=0, num_time_steps=5)

    goal_color = raw_input("Color to hunt: ")

    img = rbt.getImage()
    depth = rbt.getDepth()

    # FIND
    # Figure out what color you are looking at
    keypoints, mask = cf.findColorInImage(img, goal_color)
    # While robot is not looking at the color it is supposed to target
    while not keypoints:
        # Turn in place
        rbt.drive(0.3, 0)
        # Figure out what color you are looking at
        img = rbt.getImage()
        keypoints, mask = cf.findColorInImage(img, goal_color)

    # Found target color
    # RAM
    hit = False
    while not hit:
        # Get distance to color
        depth_image = rbt.getDepth()
        print(depth_image.size)
        print(depth_image[0][0])

        # Get error, distance and yaw

    exit()

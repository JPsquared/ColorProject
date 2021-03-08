import rospy
import cv2
import numpy as np
from turtleAPI import robot
from colorRecognition import ColorFinder
import PIDController


IMAGE_WIDTH = 640  # in pixels

if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)

    cf = ColorFinder()
    # lpid = PIDController.LinearSpeedPIDController(k_p=0.1, k_i=0.1, k_d=0, num_time_steps=5)
    apid = PIDController.AngularSpeedPIDController(k_p=0.01, k_i=0.01, k_d=0, num_time_steps=5)

    goal_color = raw_input("Color to hunt: ")

    # camera takes 480 x 640 images
    img = rbt.getImage()
    # depth = rbt.getDepth()

    # FIND
    # Figure out what color you are looking at
    keypoints, mask = cf.findColorInImage(img, goal_color)
    # While robot is not looking at the color it is supposed to target
    rbt.drive(0.3, 0)
    while not keypoints:
        # Turn in place
        rbt.drive(0.3, 0)
        # Figure out what color you are looking at
        img = rbt.getImage()
        keypoints, mask = cf.findColorInImage(img, goal_color)

    rbt.stop()
    # Found target color
    # RAM
    # may or may not use depth image
    hit = False
    counter = 0
    while not hit:
        img = rbt.getImage()
        # thought: the keypoints list may be empty sometimes
        keypoints, mask = cf.findColorInImage(img, goal_color)
        if not keypoints:
            print("Empty list")
            rbt.stop()
            continue
        else:
            print("Got something")
            print(keypoints)
            error = (IMAGE_WIDTH / 2) - keypoints[0].pt[1]
            angular_speed = apid.updateInputValue(error)
            rbt.drive(angular_speed, 0.5)

        counter += 1
        if counter == 50:
            hit = True

    exit()

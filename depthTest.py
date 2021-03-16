import rospy
import cv2
from turtleAPI import robot
from colorRecognition import ColorFinder


if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)

    rbt.drive(-0.1, 0)

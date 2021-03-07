import rospy
import cv2
from turtleAPI import robot
from colorRecognition import ColorFinder


if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)

    depth_image = rbt.getDepth()
    cv2.imshow("Depth", depth_image)
    cv2.waitKey(0)

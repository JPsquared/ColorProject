import rospy
import cv2
from turtleAPI import robot


if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)
    print("This worked")
    image = rbt.getImage()
    print(type(image))

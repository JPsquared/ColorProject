import rospy
import cv2
from turtleAPI import robot


if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)
    print("This worked")
    image = rbt.getImage()
    print(type(image))

    # spin around and take pictures
    # save all of the pictures and exit
    # separately:
    # look at the pictures with a file viewer
    # select pictures that are good examples of goal colors
    # set those pictures aside in a folder
    # set thresholds to fit around those colors

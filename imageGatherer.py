import rospy
import cv2
from time import sleep
from numpy import pi
from turtleAPI import robot


if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)

    # figure out when to stop turning
    startAngle = rbt.getAngle()

    # start turning
    rbt.drive(.2, 0)
    sleep(1)
    currentAngle = rbt.getAngle()

    # initialize cache
    imageList = []

    # start a loop to take pictures
    print(currentAngle)
    while currentAngle[2] < pi/2:
        sleep(1)
        # take a picture and add it to the cache
        imageList.append((currentAngle, rbt.getImage()))
        currentAngle = rbt.getAngle()

    # stop turning
    rbt.stop()

    # display all the cached images
    for image in imageList:
        cv2.imshow(image[0], image[1])
        cv2.waitKey(0)

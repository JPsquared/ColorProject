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
    # print(currentAngle)
    while currentAngle[2] < .9 * pi:
        sleep(1)
        # take a picture and add it to the cache
        imageList.append((str(currentAngle[2]), rbt.getImage()))
        currentAngle = rbt.getAngle()

    # stop turning
    rbt.stop()

    # display all the cached images
    print("Image List length: " + str(len(imageList)))
    for image in imageList:
        # print(type(image))
        # print(type(image[0]))
        cv2.imshow(image[0], image[1])
        sleep(0.3)
        cv2.destroyWindow(image[0])

    # balloons float in the y range 200-260 in the images

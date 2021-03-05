import rospy
import cv2
import numpy as np
from os import chdir, getcwd, listdir
from os.path import isfile, join

# Define constants
FILE_TO_TEST = "blueTest.jpg"
# divide hue number by 2 to get equivalent cv2 hue number
#    H       S       V
# [0..179, 0..255, 0..255]
LOWER_BLUE = np.array([105, 50, 20])
UPPER_BLUE = np.array([125, 255, 235])
LOWER_GREEN = np.array([35, 15, 20])
UPPER_GREEN = np.array([80, 255, 235])
LOWER_RED = np.array([])
UPPER_RED = np.array([])
LOWER_YELLOW = np.array([])
UPPER_YELLOW = np.array([])
LOWER_MAGENTA = np.array([])
UPPER_MAGENTA = np.array([])


if __name__ == "__main__":
    # want to use cv2's blob detector
    # cd to TestPhotos
    chdir("TestPhotos")
    path = getcwd()
    fileArray = [f for f in listdir(path) if isfile(join(path, f))]

    # get the filename minus '...Test.jpg'
    # for filename in fileArray:
    #     print(filename[:-8])

    img = cv2.imread(FILE_TO_TEST)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_BLUE, UPPER_BLUE)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)

    # Set up detector with default parameters
    # detector = cv2.SimpleBlobDetector()

    # Detect blobs
    # keypoints = detector.detect(blue)

    exit()

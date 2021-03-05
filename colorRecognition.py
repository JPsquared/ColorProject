import rospy
import cv2
import numpy as np
from os import chdir, getcwd, listdir
from os.path import isfile, join

# Define constants
LOWER_BLUE = np.array([210, 50, 20])
UPPER_BLUE = np.array([250, 255, 235])
LOWER_GREEN = np.array([125, 150, 200])
UPPER_GREEN = np.array([150, 255, 235])
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

    blueImg = cv2.imread("blueTest.jpg")
    # cv2.imshow('blueTest.jpg', blue)
    # cv2.waitKey(0)
    bluehsv = cv2.cvtColor(blueImg, cv2.COLOR_BGR2HSV)
    cv2.imshow('blue hsv', bluehsv)
    cv2.waitKey(0)
    bluemask = cv2.inRange(bluehsv, LOWER_GREEN, UPPER_GREEN)
    cv2.imshow('blue mask', bluemask)
    cv2.waitKey(0)

    # Set up detector with default parameters
    # detector = cv2.SimpleBlobDetector()

    # Detect blobs
    # keypoints = detector.detect(blue)

    exit()

import rospy
import cv2
import numpy as np
from os import chdir, getcwd, listdir
from os.path import isfile, join

# Define constants
LOWER_BLUE = np.array([210, 50, 20])
UPPER_BLUE = np.array([250, 255, 235])
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

    greenImg = cv2.imread("greenTest.jpg")
    # cv2.imshow('greenTest.jpg', greenImg)
    # cv2.waitKey(0)
    greenhsv = cv2.cvtColor(greenImg, cv2.COLOR_BGR2HSV)
    cv2.imshow('green hsv', greenhsv)
    cv2.waitKey(0)
    greenmask = cv2.inRange(greenhsv, LOWER_GREEN, UPPER_GREEN)
    cv2.imshow('green mask', greenmask)
    cv2.waitKey(0)

    # Set up detector with default parameters
    # detector = cv2.SimpleBlobDetector()

    # Detect blobs
    # keypoints = detector.detect(blue)

    exit()

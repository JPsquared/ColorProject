import rospy
import cv2
import numpy as np
from os import chdir, getcwd, listdir
from os.path import isfile, join


if __name__ == "__main__":
    # want to use cv2's blob detector
    # cd to TestPhotos
    chdir("TestPhotos")
    path = getcwd()
    fileArray = [f for f in listdir(path) if isfile(join(path, f))]
    # get the filename minus '...Test.jpg'
    for filename in fileArray:
        print(filename[:-8])

    blue = cv2.imread("blueTest.jpg")
    # cv2.imshow('blueTest.jpg', blue)
    # cv2.waitKey(0)
    bluehsv = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    bluemask = cv2.inRange(bluehsv, np.array([241, 15, 20]), np.array([300, 255, 235]))
    cv2.imshow('blue mask', bluemask)
    cv2.waitkey(0)

    # Set up detector with default parameters
    detector = cv2.SimpleBlobDetector()

    # Detect blobs
    # keypoints = detector.detect(blue)

    exit()

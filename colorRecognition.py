import rospy
import cv2
import numpy as np
from os import chdir, getcwd, listdir
from os.path import isfile, join
from turtleAPI import robot

# Define constants
FILE_TO_TEST = "blueTest.jpg"
# divide hue number by 2 to get equivalent cv2 hue number
#    H       S       V
# [0..179, 0..255, 0..255]
LOWER_BLUE = np.array([105, 50, 20])
UPPER_BLUE = np.array([125, 255, 235])
LOWER_GREEN = np.array([35, 50, 20])
UPPER_GREEN = np.array([80, 255, 235])
LOWER_RED = np.array([])
UPPER_RED = np.array([])
LOWER_YELLOW = np.array([])
UPPER_YELLOW = np.array([])
LOWER_MAGENTA = np.array([])
UPPER_MAGENTA = np.array([])


if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)

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
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, iterations=1)
    cv2.imshow('dilate', mask)
    cv2.waitKey(0)

    # check cv2 version
    # is_v2 = cv2.__version__.startswith("2.")
    # if is_v2:
    #     print("is_v2")
    # else:
    #     print("is_v3")

    # Set up detector
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.maxThreshold = 200
    params.minArea = 20
    params.filterByCircularity = False
    params.filterByConvexity = False
    params.filterByInertia = False
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs
    reversemask = 255 - mask
    cv2.imshow('reverse mask', reversemask)
    cv2.waitKey(0)
    keypoints = detector.detect(reversemask)
    print(keypoints)
    for k in keypoints:
        print(k.angle)
        print(type(k.pt))
        # k.pt is the center of the 'blob' in the image
        print(k.pt)
        print(k.response)
        print(k.size)

    # depthimg = rbt.getDepth()
    # print(depthimg.size)
    # print(depthimg)

    im_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)

    exit()

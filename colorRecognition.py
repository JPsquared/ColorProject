import rospy
import cv2
from os import chdir, getcwd, listdir


if __name__ == "__main__":
    print(getcwd())
    # want to use cv2's blob detector
    # cd to TestPhotos
    chdir("TestPhotos")
    path = getcwd()
    fileArray = [f for f in listdir(path)]

    blue = cv2.imread("blueTest.jpg")
    cv2.imshow('blueTest.jpg', blue)
    cv2.waitkey(0)
    exit()

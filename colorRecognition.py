import rospy
import cv2
from os import chdir, getcwd, listdir
from os.path import isfile, join


if __name__ == "__main__":
    print(getcwd())
    # want to use cv2's blob detector
    # cd to TestPhotos
    chdir("TestPhotos")
    path = getcwd()
    fileArray = [f for f in listdir(path) if isfile(join(path, f))]
    print(fileArray[1][:-8])

    blue = cv2.imread("blueTest.jpg")
    # cv2.imshow('blueTest.jpg', blue)
    # cv2.waitKey(0)
    exit()

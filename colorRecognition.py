import rospy
import cv2
from os import chdir, getcwd, listdir


if __name__ == "__main__":
    print(getcwd())
    # want to use cv2's blob detector
    # cd to TestPhotos
    chdir("TestPhotos")
    print(getcwd())
    listdir(getcwd())
    exit()

import cv2  # VM uses cv2 version '3.#'
import numpy as np
from os import chdir

# Define constants
FILE_TO_TEST = "blueTest.jpg"


class ColorFinder:

    def __init__(self):
        self.COLOR_DICT = {
            # divide hue number by 2 to get equivalent cv2 hue number
            #    H       S       V
            # [0..179, 0..255, 0..255]
            'LOWER_BLUE': np.array([105, 50, 20]),
            'UPPER_BLUE': np.array([125, 255, 235]),
            'LOWER_GREEN': np.array([35, 50, 20]),
            'UPPER_GREEN': np.array([80, 255, 235]),
            'LOWER_RED': np.array([165, 50, 20]),
            'UPPER_RED': np.array([8, 255, 235]),
            'LOWER_YELLOW': np.array([25, 50, 20]),
            'UPPER_YELLOW': np.array([35, 255, 235]),
            'LOWER_MAGENTA': np.array([145, 50, 20]),
            'UPPER_MAGENTA': np.array([158, 255, 235])
        }
        self.kernel = np.ones((3, 3), dtype=np.uint8)
        # parameters are designed to be tuned to detect specific shapes
        # many are not necessary for this project and are not included in this
        self.params = cv2.SimpleBlobDetector_Params()
        self.params.blobColor = 255  # looking for white blobs
        self.params.minThreshold = 10
        self.params.maxThreshold = 200
        self.params.minArea = 20
        self.params.filterByCircularity = False
        self.params.filterByConvexity = False
        self.params.filterByInertia = False
        self.detector = cv2.SimpleBlobDetector_create(self.params)

    def findColorInImage(self, image, color, apply_morph=True):
        """
        Returns a list of cv2.KeyPoint objects that represent areas of the input color found
        by cv2.SimpleBlobDetector

        :param numpy.ndarray image: cv2 image
        :param str color: Color to search for in image
        :param bool apply_morph: Apply cv2.morphologyEx() function to mask (default True)
        """
        color_to_test = color.upper()
        color_keys = ("LOWER_{}".format(color_to_test), "UPPER_{}".format(color_to_test))

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.COLOR_DICT[color_keys[0]], self.COLOR_DICT[color_keys[1]])
        if apply_morph:
            # pick morph
            # mask = cv2.erode(mask, kernel, iterations=1)
            # mask = cv2.dilate(mask, kernel, iterations=1)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel)
            # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, self.kernel)
        keypoints = self.detector.detect(mask)
        return keypoints, mask


if __name__ == "__main__":
    # want to use cv2's blob detector
    # cd to TestPhotos
    chdir("TestPhotos")

    # ColorToTest = FILE_TO_TEST[:-8].upper()
    # ColorKeys = ("LOWER_{}".format(ColorToTest), "UPPER_{}".format(ColorToTest))

    # img = cv2.imread(FILE_TO_TEST)  # requires being in TestPhotos directory
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv, COLOR_DICT[ColorKeys[0]], COLOR_DICT[ColorKeys[1]])
    # cv2.imshow('mask', mask)
    # cv2.waitKey(0)
    # kernel = np.ones((3, 3), np.uint8)
    # # mask = cv2.erode(mask, kernel, iterations=1)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # cv2.imshow('morphology', mask)
    # cv2.waitKey(0)

    # Set up detector
    # params = cv2.SimpleBlobDetector_Params()
    # params.blobColor = 255
    # params.minThreshold = 10
    # params.maxThreshold = 200
    # params.minArea = 20
    # params.filterByCircularity = False
    # params.filterByConvexity = False
    # params.filterByInertia = False
    # detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs
    # cv2.imshow('reverse mask', mask)
    # cv2.waitKey(0)
    # keypoints = detector.detect(mask)
    # print(keypoints)
    # for k in keypoints:
    #     print(k.angle)
    #     print(type(k.pt))
    #     # k.pt is the center of the 'blob' in the image
    #     print(k.pt)
    #     print(k.response)
    #     print(k.size)

    # depthimg = rbt.getDepth()
    # print(depthimg.size)
    # print(depthimg)

    cf = ColorFinder()
    img = cv2.imread(FILE_TO_TEST)
    goal_color = input("Color to find: ")
    keypoints, mask = cf.findColorInImage(img, goal_color)

    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)

    # Create augmented version of image
    # This works for blue
    # img[:, :, 0] = np.bitwise_or(img[:, :, 0], mask)
    img[:, :, [0, 2]] = np.bitwise_or(img[:, :, [0, 2]], mask)  # magenta?
    cv2.imshow('Augmented', img)
    cv2.waitKey(0)

    exit()

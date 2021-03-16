import cv2  # VM uses cv2 version '3.#'
import numpy as np
from os import chdir


class ColorFinder:

    def __init__(self):
        self.COLOR_DICT = {
            # divide hue number by 2 to get equivalent cv2 hue number
            #    H       S       V
            # [0..179, 0..255, 0..255]
            'LOWER_BLUE': np.array([105, 50, 20]),
            'UPPER_BLUE': np.array([125, 255, 235]),
            'LOWER_GREEN': np.array([35, 50, 20]),
            'UPPER_GREEN': np.array([80, 255, 240]),
            'LOWER_RED': np.array([165, 50, 20]),
            'UPPER_RED': np.array([8, 255, 235]),
            'LOWER_YELLOW': np.array([25, 50, 20]),
            'UPPER_YELLOW': np.array([35, 255, 235]),
            'LOWER_MAGENTA': np.array([145, 50, 20]),
            'UPPER_MAGENTA': np.array([159, 255, 245])
        }
        self.kernel = np.ones((3, 3), dtype=np.uint8)
        # parameters are designed to be tuned to detect specific shapes
        # many are not necessary for this project and are not included in this
        self.params = cv2.SimpleBlobDetector_Params()
        self.params.blobColor = 255  # looking for white blobs
        # self.params.minThreshold = 10
        # self.params.maxThreshold = 200
        # self.params.filterByArea = True
        # self.params.minArea = 20
        self.params.filterByCircularity = True
        self.params.minCircularity = 0.85
        self.params.filterByConvexity = True
        self.params.minConvexity = 0.25
        self.params.filterByInertia = True
        self.params.minInertiaRatio = 0.4
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

    def augmentImage(self, image, mask, color):
        """
        Takes an input image and a mask and applies a color filter to the image based on the mask location

        :param numpy.ndarray image: Raw image of scene
        :param numpy.ndarray mask: Masked image of scene with subject in white
        :param str color: Desired augmented color of subject
        :return numpy.ndarray: Augmented image
        """
        color_filter = {'blue': 1, 'magenta': 2, 'red': 3, 'yellow': 4, 'green': 5, 'cyan': 6}

        if color_filter[color] == 1 or color_filter[color] == 2 or color_filter[color] == 6:
            # apply blue filter
            image[:, :, 0] = np.bitwise_or(image[:, :, 0], mask)
        if color_filter[color] == 4 or color_filter[color] == 5 or color_filter[color] == 6:
            # apply green filter
            image[:, :, 1] = np.bitwise_or(image[:, :, 1], mask)
        if color_filter[color] == 2 or color_filter[color] == 3 or color_filter[color] == 4:
            # apply red filter
            image[:, :, 2] = np.bitwise_or(image[:, :, 2], mask)

        return image


if __name__ == "__main__":
    FILE_TO_TEST = "blueTest.jpg"
    # cd to TestPhotos
    chdir("TestPhotos")

    cf = ColorFinder()
    img = cv2.imread(FILE_TO_TEST)
    goal_color = raw_input("Color to find: ")
    keypoints, mask = cf.findColorInImage(img, goal_color)

    # Create augmented version of image
    img = cf.augmentImage(img, mask, goal_color)
    cv2.imshow('Augmented', img)
    cv2.waitKey(0)

    # not really necessary but the keypoint circle can be overlaid on top of the augmented image
    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)

    exit()

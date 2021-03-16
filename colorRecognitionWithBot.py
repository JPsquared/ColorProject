import rospy
import cv2
import numpy as np
from turtleAPI import robot
from colorRecognition import ColorFinder
import PIDController


IMAGE_WIDTH = 640  # in pixels

if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)

    cf = ColorFinder()
    # lpid = PIDController.LinearSpeedPIDController(k_p=0.1, k_i=0.1, k_d=0, num_time_steps=5)
    apid = PIDController.AngularSpeedPIDController(k_p=0.005, k_i=0.001, k_d=0, num_time_steps=5)

    goal_color = raw_input("Color to hunt: ")

    # camera takes 480 x 640 images
    img = rbt.getImage()

    # FIND
    # Figure out what color you are looking at
    keypoints, mask = cf.findColorInImage(img, goal_color)
    # While robot is not looking at the color it is supposed to target
    rbt.drive(0.3, 0)
    while not keypoints:
        # Turn in place
        rbt.drive(0.3, 0)
        # Figure out what color you are looking at
        img = rbt.getImage()
        keypoints, mask = cf.findColorInImage(img, goal_color)
        # display augmented image feed
        augmented = cf.augmentImage(img, mask, goal_color)
        # overlay keypoints circles onto mask for debugging purposes
        mask = cv2.drawKeypoints(mask, keypoints, np.array([]), (0, 0, 255),
                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('augmented', mask)  # replace augmented with mask to show black and white
        cv2.waitKey(10)

    rbt.stop()
    # Found target color
    # RAM
    hit = False
    saved_keypoints = []
    # counter = 0
    while not hit:
        # get what the camera is seeing
        img = rbt.getImage()
        # thought: the keypoints list may be empty sometimes
        keypoints, mask = cf.findColorInImage(img, goal_color)
        # display the augmented image feed
        augmented = cf.augmentImage(img, mask, goal_color)
        # overlay keypoints circles onto mask for debugging purposes
        mask = cv2.drawKeypoints(mask, keypoints, np.array([]), (0, 0, 255),
                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('augmented', mask)  # replace augmented with mask to show black and white
        cv2.waitKey(10)

        if not keypoints:
            # print("Empty list")
            if not saved_keypoints:
                rbt.drive(0.3, 0)
                continue
            error = saved_keypoints[0].pt[1] - (IMAGE_WIDTH / 2)
            angular_speed = apid.updateInputValue(error)
            rbt.drive(angular_speed, 0.5)
        else:
            saved_keypoints = keypoints
            error = (IMAGE_WIDTH / 2) - keypoints[0].pt[1]
            # keypoints pt, response, and size are important metrics
            angular_speed = apid.updateInputValue(error)
            print("Got Something: {} || {} || {} || {}".format(len(keypoints), keypoints[0].pt, error, angular_speed))
            rbt.drive(angular_speed, 0.5)

        # counter += 1
        # if counter == 50:
        #     hit = True
    cv2.destroyAllWindows()

    exit()

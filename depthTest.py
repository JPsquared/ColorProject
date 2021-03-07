import rospy
from turtleAPI import robot
from colorRecognition import ColorFinder


if __name__ == "__main__":
    rbt = robot()
    rate = rospy.Rate(10)

    depth_image = rbt.getDepth()
    print type(depth_image)
    print depth_image.size
    print depth_image[0][0]

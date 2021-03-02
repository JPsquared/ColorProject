import rospy
from time import sleep
from numpy import pi
from turtleAPI import robot


if __name__ == "__main__":
    rate = rospy.Rate(10)
    rbt = robot()
    startAngle = rbt.getAngle()
    # rbt.drive(.2, 0)
    sleep(1)
    currentAngle = rbt.getAngle()
    print(currentAngle)

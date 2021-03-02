import rospy
from turtleAPI import robot


if __name__ == "__main__":
    rate = rospy.Rate(10)
    rbt = robot()
    print("This worked")
    image = rbt.getImage()
    print(type(image))

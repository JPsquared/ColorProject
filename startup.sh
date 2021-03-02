#!/bin/bash

echo "$SHELL"

bash roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=/home/administrator/roblab_with_balloons.world &

echo "Gazebo launched?"
read REPLY

bash roslaunch continuous_driver continuous_driver.launch &

echo "Continuous driver launched?"
read REPLY

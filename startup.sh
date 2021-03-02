#!/bin/bash

gnome-terminal --tab --command="bash -c 'cd ~/ColorProject; $SHELL'" \
               --tab --command="bash -c 'cd ~; sleep 5; roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=/home/administrator/roblab_with_balloons.world; $SHELL'" \
               --tab --command="bash -c 'cd ~; sleep 6; roslaunch continuous_driver continuous_driver.launch; $SHELL'"

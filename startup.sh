#!/bin/bash

gnome-terminal --tab --command="bash -c 'cd ~/ColorProject; ls; $SHELL'" \
               --tab --command="bash -c 'cd ~; roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=/home/administrator/roblab_with_balloons.world; $SHELL'" \
               --tab --command="bash -c 'sleep 5; cd ~; roslaunch continuous_driver continuous_driver.launch; $SHELL'"

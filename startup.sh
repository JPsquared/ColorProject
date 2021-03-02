#!/bin/bash

gnome-terminal --tab --title="Shell" --command="bash -c 'cd ~; ls; $SHELL'" --tab --title="Gazebo" --command="bash -c 'cd ~; roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=/home/administrator/roblab_with_balloons.world; $SHELL'" --tab --title="Driver" --command="bash -c 'cd ~; roslaunch continuous_driver continuous_driver.launch; $SHELL'"

#!/bin/bash

gnome-terminal --tab --command="bash -c 'cd ~/ColorProject; $SHELL'" \
               --tab --command="bash -c 'cd ~; source ~/turtleAPI/bashrc; balloonRoom; $SHELL'" \
               --tab --command="bash -c 'cd ~; source ~/turtleAPI/bashrc; turtleLegs; $SHELL'" \
               --tab --command="bash -c 'cd ~; source ~/turtleAPI/bashrc; googleMap; $SHELL'"

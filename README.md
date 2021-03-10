# ColorProject

### [Informational PDF](https://www.usna.edu/Users/cs/taylor/courses/si475/notes/cameras.pdf)

### [Instructions](https://www.usna.edu/Users/cs/taylor/courses/si475/hw/balloons.html)

### [World File](https://www.usna.edu/Users/cs/taylor/courses/si475/resources/roblab_with_balloons.world)

### [PID Controller PDF](https://www.usna.edu/Users/cs/taylor/courses/si475/notes/pid.pdf)

### [Turtle API](https://www.usna.edu/Users/cs/taylor/courses/si475/hw/turtleAPI.html)

In your program, you should be able to type in a color, and the robot will find and ram the balloon of that color.

Restrictions:

- You may not hard code in balloon locations - this should be using the camera only.
- You must display an augmented-reality version of your camera feed at all times that demonstrates which pixels are 
  being identified as your balloon (for example, make the red balloon pixels unnaturally red to be clear they’ve been 
  identified).
- You must home in on your balloon using a PID controller to keep the balloon in the center of the image.
- You may not reference the balloon colors using Gazebo - you have to extract these using saved images and some external
  program.
  

#### Startup.sh and ColorProjectStartup.desktop

`startup.sh` was created to make initialising the various terminals simpler. It runs the four commands needed to prepare
the project environment to run tests.

`ColorProjectStartup.desktop` was created to be placed on the desktop so that when it is run, `startup.sh` will be run. 
This must be made to be executable using chmod along with `startup.sh`.
# camera_ws
Trial and Error repo for reading image from camera & publishing.

# Packages Used
## v4l2_camera
A ROS2 Camera driver package. [Look here for repo](https://github.com/tier4/ros2_v4l2_camera/tree/galactic)

[This article](https://medium.com/swlh/raspberry-pi-ros-2-camera-eef8f8b94304) details how to build and run this package. It focuses on Raspberry Pi OS with the Raspberry Pi Camera Module V2 but should generalise for most systems. 

I have already compiled the command lines to run in the following sections so you don't have to view the article unless you are curious.

### Install & Run Camera Driver
Inside workspace run:

        git clone --branch humble https://gitlab.com/boldhearts/ros2_v4l2_camera.git
        git clone --branch humble https://github.com/ros-perception/vision_opencv.git
        git clone --branch humble https://github.com/ros-perception/image_common.git
        git clone --branch humble https://github.com/ros-perception/image_transport_plugins.git
        cd ..
        rosdep install --from-paths src -r -y

        colcon build --packages-up-to v4l2_camera image_transport_plugins
        source install/local_setup.bash

### Building: Ubuntu
The following packages are required to be able to build the plugins:

        sudo apt install libtheora-dev libogg-dev libboost-python-dev

### Usage
Publish camera images, using the default parameters:

        ros2 run v4l2_camera v4l2_camera_node

Preview the image (open another terminal):

        ros2 run rqt_image_view rqt_image_view

Next, navigate into ~/camera_ws/src/ros2_v4l2_camera package and change the code in parameters.cpp 

Find

        video_device - string, default: "/dev/video0" (default is 0, which is your laptop webcam)

And make the following change

        /dev/video0 to /dev/video2 (USB Camera)

## Running of Nodes

        cd ~/camera_ws/
        colcon build
        source install/setup.bash
        ros2 run v4l2_camera v4l2_camera_node

Open new terminal to run video processor node.
        
        ros2 run camera cam_process

Open new terminal to run rqt to view images.

        rqt

Open new terminal to run rqt_graph to view nodes and topics.

        rqt_graph

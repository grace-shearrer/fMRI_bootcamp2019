# fMRI_bootcamp2019


This is all the things you need and probably more for the UNC fMRI_bootcamp2019. Please keep in mind this is usually at minimum a 1 week course. It is an entire PhD for others. We are going to fly fast and loose but at the end you should have a general idea why preprocessing steps are taken and how to create GLMs.

# Get Docker!
This is going to allow us to all be working off the same slides and operating systems.
https://docs.docker.com/docker-for-mac/

# Get VNC viewer
https://www.realvnc.com/en/connect/download/viewer/

# Pull my docker image!
docker pull gshearrer/fmribootcamp:0.05

This is gonna take a minute. While you are waiting brush up on linux!
http://www.ee.surrey.ac.uk/Teaching/Unix/

# Open a terminal and type the following
open -a XQuartz  
IP=$(ifconfig en1 | grep inet | awk '$1=="inet" {print $2}')  
xhost + $IP  


# Test the docker
docker run --rm -it  -p 5901:5901 gshearrer/fmribootcamp:0.05 xterm

## You should now have a vnc running
Open your vnc viewer and type 127.0.0.1:5901
It will ask you for a password: graceiscool
You should have a plain grey desktop. If you click the desktop a terminal window will appear. Test the install by typing the following the in VNC terminal (not your local terminal)

fsl &

You should now have the fsl GUI on the desktop. If that is working you are all good! If not..... contact me.
If that is all good (or if it isn't but you want to stop) type
exit
in the vnc terminal

# Feeling advanced you can play with this and test the jupyter notebooks
## Note you need to change the path to your machine
docker run --rm -it -p 8888:8888  -p 5901:5901 -v /Users/gracer/Google\ Drive/fMRI_workshop/2019/4dock/notebooks/:/home/jovyan/work gshearrer/fmribootcamp:0.05 xterm

docker ps -a

docker exec -it a995c3ff00ca  bash

jupyter notebook --allow-root

# Base Jupyter Notebook Stack

Please visit the documentation site for help using and contributing to this image and others.

* [Jupyter Docker Stacks on ReadTheDocs](http://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)
* [Selecting an Image :: Core Stacks :: jupyter/base-notebook](http://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-base-notebook)

# Build with Neurodocker

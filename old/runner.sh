#!/bin/bash
docker build -t gshearrer/fmribootcamp:0.05 .

docker push gshearrer/fmribootcamp:0.05

open -a XQuartz
IP=$(ifconfig en1 | grep inet | awk '$1=="inet" {print $2}')
xhost + $IP

docker run --rm -it -p 5901:5901 gshearrer/fmribootcamp:0.05 xterm

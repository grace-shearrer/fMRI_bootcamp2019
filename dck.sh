#!/bin/bash

docker build -t gshearrer/fmribootcamp:0.04 .

docker push gshearrer/fmribootcamp:0.04

docker run -it --rm \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-p 8888:8888 \
--entrypoint /bin/bash \
gshearrer/fmribootcamp:0.04
#!/bin/bash
docker build -t gshearrer/fmribootcamp:0.05 .

docker push gshearrer/fmribootcamp:0.05


docker run --rm -it -p 5901:5901 gshearrer/fmribootcamp:0.05 xterm

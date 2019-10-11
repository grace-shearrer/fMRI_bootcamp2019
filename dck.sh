#!/bin/bash

docker build -t gshearrer/fmribootcamp:0.04 .

docker push gshearrer/fmribootcamp:0.04

docker run -it --rm -p 8888:8888 --entrypoint /bin/bash gshearrer/fmribootcamp:0.04

#!/bin/bash
docker run --rm kaczmarj/neurodocker:0.6.0 generate docker \
 --base=debian:stretch --pkg-manager=apt \
  --install git \
  --vnc passwd=graceiscool start_at_runtime=true geometry=1920x1080 \
  --install xterm \
  --fsl version=5.0.10 method=binaries \
  --miniconda create_env=neuro \
              conda_install='numpy traits' \
  --miniconda use_env=neuro \
              conda_install='jupyter' \
              miniconda_version="4.3.31" \
  -o Dockerfile \
  >> Dockerfile


docker build -t gshearrer/fmribootcamp:0.05 .

docker push gshearrer/fmribootcamp:0.05

open -a XQuartz
IP=$(ifconfig en1 | grep inet | awk '$1=="inet" {print $2}')
xhost + $IP

#docker run -it --rm \
#-e DISPLAY=$IP:0 \
#-v /tmp/.X11-unix:/tmp/ \
#-p 5901:55901 \
#--entrypoint /bin/bash \
#gshearrer/fmribootcamp:0.05 \
#xterm

docker run --rm -it -p 5901:5901 gshearrer/fmribootcamp:0.05 xterm

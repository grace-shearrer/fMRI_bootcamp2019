docker pull gshearrer/fmribootcamp:0.05

open -a XQuartz
IP=$(ifconfig en1 | grep inet | awk '$1=="inet" {print $2}')
xhost + $IP

docker build -t gshearrer/fmribootcamp:0.05 .

docker run --rm -it -p 8888:8888  -p 5901:5901 -v /Users/gracer/Google\ Drive/fMRI_workshop/2019/4dock/notebooks/:/home/jovyan/work gshearrer/fmribootcamp:0.05 xterm

docker ps -a

docker exec -it a995c3ff00ca  bash

jupyter notebook --allow-root

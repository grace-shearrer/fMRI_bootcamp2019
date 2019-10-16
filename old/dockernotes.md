# Docker stuff

## Get name with
docker ps -a

## Delete image
docker rmi <image name>

## Stop containers
docker stop

## Remove stopped containers and unused images
docker system prune -a

## Remove containers
docker rm ID_or_Name ID_or_Name

## DISPLAY
open -a XQuartz
IP=$(ifconfig en1 | grep inet | awk '$1=="inet" {print $2}')
xhost + $IP

## vnc
https://www.realvnc.com/en/connect/download/viewer/macos/

## Data
aws s3 sync --no-sign-request s3://openneuro.org/ds000001 ds000001-download/
datalad install https://github.com/OpenNeuroDatasets/ds000001.git

##Linux tutorial

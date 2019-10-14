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

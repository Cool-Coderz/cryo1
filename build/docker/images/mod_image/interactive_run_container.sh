#!/bin/bash

# run container
IMAGE_NAME="cent76_conda3_mod_run"
CONTAINER_NAME="cc_mod"

# remove previous containers first
###AF_CONT=$(docker ps -a | grep $CONTAINER_NAME)
#ARR=($AF_CONT)
#CONTAINER_ID=${ARR[0]}
#if [ -z CONTAINER_ID ]
#then
#	echo "docker rm ${CONTAINER_ID}"
#	docker stop $CONTAINER_ID
#	docker rm $CONTAINER_ID
#fi

# run new container from iamge
#docker run -d -p 443:443 -p 8008:8008 --name $CONTAINER_NAME $IMAGE_NAME
docker exec -it $CONTAINER_NAME bash

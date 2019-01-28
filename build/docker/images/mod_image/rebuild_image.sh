#!/bin/bash

IMAGE_NAME="cent76_conda3_mod_run"
CONTAINER_NAME="cc_mod"

# remove previous containers first
echo "docker ps -a | grep $CONTAINER_NAME"
docker ps -a | grep $CONTAINER_NAME
AF_CONT=$(docker ps -a | grep $CONTAINER_NAME)
echo "AF_CONT: $AF_CONT"
if [ -z AF_CONT ]
then
    ARR=($AF_CONT)
    echo "ARR: $ARR"
    CONTAINER_ID=${ARR[0]}
    echo "CONT ID: $CONTAINER_ID"
    if [ -z CONTAINER_ID ]
    then
	echo "attempting to stop and rum container"
	docker stop $CONTAINER_ID
	docker rm $CONTAINER_ID
    fi
fi


docker build --tag $IMAGE_NAME .

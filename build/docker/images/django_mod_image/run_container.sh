#!/bin/bash

# run container
IMAGE_NAME="cent76_conda3_django194_mod"
CONTAINER_NAME="django194_mod"

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

# run new container from iamge
echo "docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
echo "docker exec -it ${CONTAINER_NAME} /bin/bash"
docker run -d -p 8000:8000 --name $CONTAINER_NAME $IMAGE_NAME

docker top $CONTAINER_NAME
docker logs $CONTAINER_NAME

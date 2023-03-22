#!/bin/bash

# get the docker repository
$DOCKER_REPO=$DOCKER_REPO
$DOCKER_USERNAME=$DOCKER_USERNAME
$DOCKER_PASSWORD=$DOCKER_PASSWORD

# build image
docker build -f ./homework3/solution/logging/Dockerfile -t logging:latest ./homework3/solution/logging

# tag image
docker tag logging:latest $DOCKER_REPO:latest

# docker login
docker login --username=$DOCKER_USERNAME --password=$DOCKER_PASSWORD

# publish image
docker push $DOCKER_REPO:latest
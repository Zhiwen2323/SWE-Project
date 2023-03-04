#!/bin/bash

# get the docker repository
$DOCKER_REPO=$DOCKER_REPO

# build image
docker build -f ./homework2/docker/ui.Dockerfile -t ui:latest ./homework1/ui

# tag image
docker tag ui:latest $DOCKER_REPO:latest

# publish image
docker push $DOCKER_REPO:latest
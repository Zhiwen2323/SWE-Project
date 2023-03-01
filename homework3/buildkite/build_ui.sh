#!/bin/bash


# build image
docker build -f ./homework2/docker/ui.Dockerfile -t ui:latest ./homework1/ui

# tag image
docker tag ui:latest gcr.io/zhiwenswe/ui:latest

# publish image
docker push gcr.io/zhiwenswe/ui:latest
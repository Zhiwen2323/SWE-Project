#!/usr/bin/env bash

set -euo pipefail

manifest="$(mktemp)"
DOCKER_REPO=$DOCKER_REPO

echo '--- :kubernetes: Shipping'

APP="./homework2/kubernetes/ui/deployment.yaml"
IAMGE_ID="$DOCKER_REPO:latest"
envsubst < $APP | kubectl apply -f -

echo '--- :zzz: Waiting for deployment'
kubectl wait --for condition=available --timeout=300s -f $APP

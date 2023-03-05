#!/usr/bin/env bash

set -euo pipefail

manifest="$(mktemp)"
DOCKER_REPO=$DOCKER_REPO

echo '--- :kubernetes: Shipping'

APP="./homework2/kubernetes/ui/deployment.yaml"
export IMAGE_ID="$DOCKER_REPO:latest"
envsubst < $APP | kubectl apply -f -
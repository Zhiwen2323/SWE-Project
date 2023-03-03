#!/usr/bin/env bash

set -euo pipefail

manifest="$(mktemp)"

echo '--- :kubernetes: Shipping'

APP="./homework2/kubernetes/ui/deployment.yaml"
kubectl apply -f $APP

echo '--- :zzz: Waiting for deployment'
kubectl wait --for condition=available --timeout=300s -f $APP

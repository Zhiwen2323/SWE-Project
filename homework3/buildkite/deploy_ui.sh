#!/usr/bin/env bash

set -euo pipefail

manifest="$(mktemp)"

echo '--- :kubernetes: Shipping'

ls

kubectl apply -f ./homework2/kubernetes/ui/deployment.yaml

echo '--- :zzz: Waiting for deployment'
kubectl wait --for condition=available --timeout=300s -f ./homework2/kubernetes/ui/deployment.yaml

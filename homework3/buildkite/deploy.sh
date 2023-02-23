#!/usr/bin/env bash

set -euo pipefail

if [ -z "${DOCKER_IMAGE:-}" ]; then
  echo ":boom: \$DOCKER_IMAGE missing" 1>&2
  exit 1
fi

manifest="$(mktemp)"

echo '--- :kubernetes: Shipping'

ls

envsubst < ./homework2/kubernetes/ui/deployment.yml > "${manifest}"
kubectl apply -f "${manifest}"

echo '--- :zzz: Waiting for deployment'
kubectl wait --for condition=available --timeout=300s -f "${manifest}"

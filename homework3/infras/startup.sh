#!/bin/bash

KUBE_CLUSTER_NAME=chatgpt
KUBE_CLUSTER_ZONE=us-east1-b
AGENT_TOKEN="$1"

CURRENT_DIR="$( cd "$( dirname "$0" )" && pwd )"

# Get kubernetes config
gcloud container clusters get-credentials $KUBE_CLUSTER_NAME --zone $KUBE_CLUSTER_ZONE

# Create buildkite agent secret
kubectl delete secret buildkite-agent --ignore-not-found
kubectl create secret generic buildkite-agent --from-literal=token=$AGENT_TOKEN

# create service account
kubectl apply -f $CURRENT_DIR/sa.yaml

# start buildkite-agent
kubectl apply -f $CURRENT_DIR/buildkite-agent.yaml


# install rabbitmq kubernetes operator
kubectl apply -f "https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml"

# create rabbitmq cluster
kubectl apply -f $CURRENT_DIR/logging_rabbit.yaml
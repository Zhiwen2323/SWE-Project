#!/bin/bash

KUBE_CLUSTER_NAME=$KUBE_CLUSTER_NAME
KUBE_CLUSTER_ZONE=KUBE_CLUSTER_ZONE
AGENT_TOKEN=$AGENT_TOKEN

# Get kubernetes config
gcloud container clusters get-credentials $KUBE_CLUSTER_NAME --zone $KUBE_CLUSTER_ZONE

# Create buildkite agent secret
kubectl create secret generic buildkite-agent --from-literal=token=$AGENT_TOKEN

# create service account
kubectl apply -f sa.yaml

# start buildkite-agent
kubectl apply -f buildkite-agent.yaml


# install rabbitmq kubernetes operator
kubectl apply -f "https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml"

# create rabbitmq cluster
kubectl apply -f logging_rabbit.yaml
#!/bin/bash

# Download the latest version of kubectl
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"

# Make the kubectl binary executable
chmod +x kubectl

# Move the kubectl binary to a directory in your PATH
sudo mv kubectl /usr/local/bin/
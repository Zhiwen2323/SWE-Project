#!/bin/bash

# Install required packages
apt-get update
apt-get install -y nodejs mysql-server python3-pip

# Link python to python3
ln -s /usr/bin/python3 /usr/bin/python

# Start mysql service
service mysql start

# Install React and ReactDOM as dependencies
npm install react react-dom

# Install Flask and OpenAI
pip3 install aiohttp flask flask-cors flask-mysql openai flask-session

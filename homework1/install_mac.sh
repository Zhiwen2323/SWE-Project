#!/bin/bash

# check if Homebrew is installed
if ! command -v brew > /dev/null; then
  echo "Homebrew is not installed. Please install it first."
  echo "To install brew, run below command in terminal:"
  echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"'
  exit 1
fi

# Install Xcode Command Line Tools
if [[ $xcode_check == *"version"* ]]; then
  echo "Xcode Command Line Tools are installed."
else
  echo "Xcode Command Line Tools are not installed. installing it now."
  xcode-select --install
fi

# alias python to python3 to ensure we are using python3
alias python=python3

# install Node.js using Homebrew
brew install node

# install mysql
brew install mysql

# start mysql service
brew services start mysql

# install React and ReactDOM as dependencies
npm install react react-dom

# install flask & openai
pip3 install aiohttp flask flask-cors flask-mysql openai flask-session pika


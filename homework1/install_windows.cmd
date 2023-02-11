@echo off

rem Check if Python 3 is installed
python -V >nul 2>&1 || (echo "Python 3 is not installed. Please install it first." & exit /b 1)

rem Check if Node.js is installed
node -v >nul 2>&1 || (echo "Node.js is not installed. Installing it now." & goto install_node)

:install_node
rem Install Node.js
npm install -g node

rem Install MySQL
rem (You may need to download the installer from the official website and install it manually)

rem Start MySQL Service
rem (You may need to start the service manually through the services control panel)

rem Install React and ReactDOM as dependencies
npm install -g react react-dom

rem Install Flask and OpenAI
pip install aiohttp flask flask-cors flask-mysql openai flask-session

echo Script completed successfully.




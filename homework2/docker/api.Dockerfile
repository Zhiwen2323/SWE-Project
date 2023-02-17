# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to the container
# TODO: create the requirements.txt at your homework1/api
COPY requirements.txt ./

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Specify the command to run when the container starts
# TODO: finish the CMD here


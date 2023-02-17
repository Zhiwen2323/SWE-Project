# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package*.json ./

# Install the required dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Build the React application
RUN npm run build

# Expose port
Expose 3000

# Specify the command to run when the container starts
CMD [ "npm", "start" ]

# Homework 2 - Infrastructure and Devops
This homework is meant to help you get familiar with docker, kubernetes and buildkite, and use it to build your chatgpt application.

## Tasks
The main task is to finish the docker and kubernetes for the ui and api. \
In the meanwhile, in order to make the ui and api functional, you need to
update the homework1:

1. Create [requirements.txt](https://learnpython.com/blog/python-requirements-file/) in homework1/api to include required libraries for
the api.
2. Update the `fetch` api endpoint in the UI to use kubernetes cluster endpoint.
e.g, if your ui `service` name is react-ui, then its exposed endpoint will be ` http://react-ui:3000`
3. Add your api buildkite pipeline steps in the buildkite/api.yaml

## Grading Criteria

1. Functionality of your Dockfile and kubernetes deployment.yaml
2. buildkite steps to be able to build and deploy api
# Setup ui buidkite pipeline
In homework 2, we have a ui deployment pipeline using your local buildkite agent.
We need to update it to work with your GCP buildkite agent.

## Instructions
1. 
2. Update Command to run to point to ui deployment yaml:
`buildkite-agent pipeline upload homework3/buildkite/ui/buildkite.yaml`
Also give an environment variable:
DOCKER_REPO=<your docker repo name>
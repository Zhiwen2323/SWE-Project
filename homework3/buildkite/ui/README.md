# Setup ui buidkite pipeline
In homework 2, we have a ui deployment pipeline using your local buildkite agent.
We need to update it to work with your GCP buildkite agent.

## Instructions
1. In your ui pipeline, update Command to run to point to ui deployment yaml:
`buildkite-agent pipeline upload homework3/buildkite/ui/buildkite.yaml`
Also give environment variables as docker credentials:
DOCKER_REPO=<your_docker_repo>
DOCKER_USERNAME=<your_docker_username>
DOCKER_PASSWORD=<your_docker_password>
![buildkite_pipeline.png](..%2F..%2Finfras%2Fimages%2Fbuildkite_pipeline.png)
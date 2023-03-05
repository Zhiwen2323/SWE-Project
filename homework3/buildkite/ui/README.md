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

2. Update docker images in `homework2/kubernetes/ui/deployment.yaml` and `homework2/kubernetes/api/deployment.yaml` to use
$IMAGE_ID which will use the environment variable to point to the remote docker image. you will also need to update the 
`imagePullPolicy: Never` to `imagePullPolicy: Always`. \
`homework2/kubernetes/ui/deployment.yaml` has already been updated for you.

3. your UI pipeline should look like below:
![buildkite_ui_pipeine.png](..%2F..%2Finfras%2Fimages%2Fbuildkite_ui_pipeine.png)
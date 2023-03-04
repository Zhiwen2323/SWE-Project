# Move to the cloud

## Instruction
1. First start a kubernetes cluster in Google Cloud Platform following the instruction at
2. After Cluster startup, shell into the cluster
3. Run `./homework3/infras/startup.sh` to setup required infras
4. In buildkite, update your UI and API pipelines to point to `homework3/buildkite` \

After that you should be able to have an continuous delivery to the Google cloud kubernetes cluster

## Tasks
1. Finish the `homework3/buildkite/api/` following the ui.
2. Add logging into homework1
3. Finish the TODO in `./homework3/logging/logging/log_worker` to make the log worker runnable.
4. Update the `./homework3/logging/deployment.yaml` to automatically deploy the log worker in kubernetes cluster
5. Update the kubernetes networking to expose chatgpt UI to the internet.

## Submission

## Grading Criteria
1. Able to view and use the chatgpt UI
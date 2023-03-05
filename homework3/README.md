# Move to the cloud

## Instruction
1. First start a kubernetes cluster in Google Cloud Platform following the instruction at [infra README](./infras/README.md)
2. In buildkite, update your UI and API pipelines to point to `homework3/buildkite/ui/buildkite.yaml` and `homework3/buildkite/api/buildkite.yaml` (
you need to create this one). more instructions go to [buildkite README](./buildkite/ui/README.md) \
After that you should be able to have an continuous delivery to the Google cloud kubernetes cluster

## Tasks
### UI & API
1. Finish the `homework3/buildkite/api/` following the `homework3/buildkite/ui/`.

### Logging
1. Add logging functionality into homework1. More instructions is in
2. Finish the TODO in `./homework3/logging/logging/log_worker` to make the log worker runnable.
4. Update the `./homework3/logging/deployment.yaml` to automatically deploy the log worker in kubernetes cluster
5. Update the kubernetes networking to expose chatgpt UI to the internet.

## Submission

## Grading Criteria
1. Able to view and use the chatgpt UI
# Move to the cloud

## Instruction
1. First start a kubernetes cluster in Google Cloud Platform following the instruction at [infra README](./infras/README.md)
2. In buildkite, update your UI and API pipelines to point to `homework3/buildkite/ui/buildkite.yaml` and `homework3/buildkite/api/buildkite.yaml` (
you need to create this one). More instructions go to [buildkite README](./buildkite/ui/README.md) \
After that you should be able to have an continuous delivery to the Google cloud kubernetes cluster

## Tasks
### UI & API
1. Following the [buildkite README](./buildkite/ui/README.md) make the UI continuous delivery work. 
2. Create the API continuous delivery pipeline at `homework3/buildkite/api/` by following the `homework3/buildkite/ui/`.

### Logging System
Support the logging functionality.
1. Update `homework1/api/app.py` to finish the functionality to publish to rabbitMQ cluster.
2. Finish the logging worker app. More instructions are in [logging README](./logging/README.md)
3. Create the logging worker app continuous delivery pipeline at `homework3/buildkite/logging/` 

## Submission
Submit your code into your fork repository

## Grading Criteria
1. Able to view and use the chatgpt UI.
3. Able to write log to GCS. we will use it in the next homework.
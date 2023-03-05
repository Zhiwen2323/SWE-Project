# Logging system
This describe the tasks to build a logging system.

## Tasks
1. Following the way we build the UI and API buildkite pipeline, create a continuous deployment pipeline
for logging system. please write the your deployment files in `homework3/logging/`
2. Finish the functionality in `log_worker.py`, you might also want to update the `ConnectionParameters('localhost')`
to the true rabbitMQ connection endpoint. (hint, What is the rabbitMQ cluster name, and how do we find it?)
3. Finish the TODO in log_worker.py
4. You will need to create a Dockerfile like what you do for the API.
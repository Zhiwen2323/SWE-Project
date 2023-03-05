# Infrastructure setups

## How to create kubernetes cluster in GCP
1. Create the cluster in GCP console
![cluster_view.png](images%2Fcluster_view.png)

2. Choose Standard: You manage your cluster
![create_cluster_view.png](images%2Fcreate_cluster_view.png)

3. Configure: \
Name: chatgpt \
Zone: us-east1-b \
![cluster_config_view.png](images%2Fcluster_config_view.png)

4. Click CREATE

## How to use Docker Hub to pull and push your docker images
1. Open Docker Hub and signup or login to your docker hub account at https://hub.docker.com/
2. Create a public repository and specify a name such as chatgpt-ui
![docker_create_repo.png](images%2Fdocker_create_repo.png)


## How to install required infras
1. Connect to your cluster by clicking CONNECT:
![connect_cluster.png](images%2Fconnect_cluster.png)
2. Then click Run in cloud shell
3. Type ENTER in terminal to execute the command and authorize.
4. git clone repository and cd into it
5. Simply run `./homework3/infras/startup.sh <BUILDKITE_AGENT_TOKEN>` with your buildkite agent token to startup all
required infras including buildkite agent and rabbitmq cluster.

## How to expose kubernetes service into internet
We will simplify the process to expose the service to internet
1. First go to the GCP console and click Service & Ingress which will show all the service that can routed to the internet
![kubernetes_service.png](images%2Fkubernetes_service.png)
2. 
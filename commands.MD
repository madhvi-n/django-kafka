# Commands used for docker and kubernetes
***

##### To build containers
`docker compose build`

##### To start docker containers
`docker compose up -d`
`-d stands for detached which means containers keep running in background`

##### To stop and remove container
`docker stop <container_name>`
`docker remove <container_name>`

##### Remove dangling docker images
`docker image prune`

##### Deleting a docker image
`docker image rm <image_name>:<tag>`

##### To create a project image and push to docker hub
`Assuming you have already image created and docker hub credentials`
- Login
`docker login`
<br/>

- Tag the docker image
  `docker image tag <image_name>:<tag> <username>/<image_name>:<tag>`
  `docker image tag django_kafka_crud-django:latest mayascarlet31/django_kafka_crud-django:latest`
<br/>

- Push the docker image
`docker image push <username>/<image_name>:<tag>`


##### To fetch IP address of a docker container
`docker container inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>`

##### To execute command inside a docker container
`docker exec <container_name_or_id> hostname -i`

##### For running shell inside docker container
`docker exec -it <container_name_or_id> bash`

##### Checking database
`psql -U <postgres_user> -d <database_name>`

##### Start kubernetes cluster using minikube
`minikube start`

##### Access Kubernetes dashboard
`minikube dashboard`


##### Check cluster info and status
`minikube status`
`kubectl cluster-info`


##### Apply manifest.yaml to kubernetes
`kubectl apply -f <manifest.yaml>`
`kubectl apply -f <directory>`

##### Delete deployment
`kubectl delete deployment deployment_name`


##### Delete and apply deployment
`kubectl create -f deployment.yaml`
`kubectl apply -f deployment.yaml`

##### To fetch info
`kubectl get deployments`
`kubectl get pods`
`kubectl get replicasets`

##### To get detailed info about deployment and pods
`kubectl describe deployment <deployment_name>`
`kubectl describe pods -l app=<deployment_name>`

#### Get logs
`kubectl logs deployment-name-pod-name`


##### Scale a deployment
`kubectl scale deployment my-deployment --replicas=3`

##### Delete replicasets
`kubectl delete replicaset my-empty-replicaset`

##### To check data produced using Kafka Producer
`docker exec -it <kafka_container_name> kafka-console-consumer --bootstrap-server <bootstrap_servers> --topic <topic_name> --from-beginning

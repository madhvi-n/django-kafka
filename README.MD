# Django-Kafka
Django CRUD application integrated with Kafka messaging system for efficient asynchronous data processing and near real-time updates.


## Project requirements
- Python 3.8+
- Docker

## Running the project
 - Build the docker images defined in docker compose file and start the containers in detached mode (in the background)
`docker compose build && docker compose up -d`


- Access the students api at the endpoint `http://localhost:8000/api/v1/students/`



### Summary of the configuration(what each file does):
**Dockerfile**:
- Sets the base image as Python 3.10.
- Sets environment variables.
- Sets the working directory.
- Copies the requirements.txt file and installs project dependencies.
- Copies all project files.
- Exposes port 8000.
- Defines the CMD instruction to run migrations and start the Django development server.

**docker-compose.yml**:
- Defines multiple services including `Redis`, `PostgreSQL`, `ZooKeeper`, `Kafka`, and `Django`.
- Configures the necessary environment variables for each service.
- Maps ports for `PostgreSQL`, `ZooKeeper`, and `Kafka`.
- Specifies dependencies using the `depends_on` directive.
- Defines a volume for the PostgreSQL data.

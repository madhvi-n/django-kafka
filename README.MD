# Django Kafka CRUD
Django Kafka CRUD is a Django-based CRUD application integrated with Kafka messaging system for asynchronous data processing. It allows you to save and retrieve student records using REST endpoints. The application leverages Kafka to ensure efficient handling of data-intensive tasks and provides near real-time updates.

[![Django CI](https://github.com/madhvi-n/store-monitoring/actions/workflows/django.yml/badge.svg)](https://github.com/madhvi-n/store-monitoring/actions/workflows/django.yml)


## Project requirements
- Python 3.10
- Docker

## Installation
- Clone the repository `git clone https://github.com/madhvi-n/django-kafka-crud.git`

- Navigate to project directory `cd django_kafka_crud`


- Create a virtual environment `virtualenv venv --python=python3`

- Activate the virtual environment `source venv/bin/activate`

- Install the project dependencies `pip install -r requirements.txt`


- Create a `.env` file in the root directory of the project and configure the required environment variables. Refer to the .env.example file for the list of variables and their sample values.


 - Build the docker images defined in docker compose file and start the containers in detached mode (in the background) `docker compose build && docker compose up -d`


- Access the students api at the endpoint `http://localhost:8000/api/v1/students/`


- The application should now be running locally. Access it in your web browser at `http://localhost:8000`.



## Summary of the configuration(what each file does):
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

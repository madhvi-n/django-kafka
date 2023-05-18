import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_kafka_crud.settings')

app = Celery('django_kafka_crud')
app.conf.task_default_queue = 'django_kafka_crud_queue'
app.conf.task_default_exchange = 'django_kafka_crud_exchange'
app.conf.task_default_routing_key = 'django_kafka_crud'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

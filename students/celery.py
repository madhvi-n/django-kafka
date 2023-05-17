import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_kafka_crud.settings')

app = Celery('django_kafka_crud')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

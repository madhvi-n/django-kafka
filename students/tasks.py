from celery import shared_task
from .kafka_util import fetch_data_from_kafka
from django.db import transaction
from students.models import Student
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
from django.conf import settings
import json
import logging

logger = logging.getLogger(__name__)

@shared_task
def process_kafka_messages():
    try:
        fetch_data_from_kafka()
    except Exception as e:
        logger.error("Celery task error: %s", str(e))

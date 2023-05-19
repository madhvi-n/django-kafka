from celery import shared_task
from core.services import fetch_data_from_kafka
import logging

logger = logging.getLogger(__name__)

@shared_task
def process_kafka_messages():
    try:
        fetch_data_from_kafka()
    except Exception as e:
        logger.error("Celery task error: %s", str(e))

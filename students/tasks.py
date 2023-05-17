from celery.decorators import periodic_task
from datetime import timedelta

@periodic_task(run_every=timedelta(minutes=1))
def process_kafka_messages():
    # Kafka message processing logic here
    # Save messages to the database

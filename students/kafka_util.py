from kafka import KafkaProducer
from kafka.errors import KafkaError
from django.conf import settings
import json


def send_data_to_kafka(data):
    producer = KafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
    producer.send(settings.KAFKA_TOPIC, value="Data from server")
    producer.flush()  # Optional: Ensure all messages are sent
    producer.close()  # Optional: Close the producer

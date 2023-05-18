from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
from django.conf import settings
import json


def send_data_to_kafka(data):
    producer = KafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS
    )
    json_data = json.dumps(data)
    value_bytes = json_data.encode("utf-8")
    producer.send(settings.KAFKA_TOPIC, value=value_bytes)
    producer.flush()  # Optional: Ensure all messages are sent
    producer.close()  # Optional: Close the producer


def fetch_data_from_kafka():
    consumer = KafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id='student_consumer_group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    fetched_data = []
    for message in consumer:
        data = message.value  # Decode the message value
        fetched_data.append(data)
        print(f"Fetched data from Kafka: {data}")

    consumer.close()
    return fetched_data

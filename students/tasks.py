from celery import shared_task
from .kafka_util import fetch_data_from_kafka
from django.db import transaction
from students.models import Student


@shared_task
def process_kafka_messages():
    try:
        # Kafka message processing logic here
        while True:
            data = fetch_data_from_kafka()
            if data is None:
                break

            print(f"Data from Kafka: {data}")
            print(data['first_name'])
            try:
                with transaction.atomic():
                    student, created = Student.objects.get_or_create(
                        first_name=data['first_name'], last_name=data['last_name'],
                        age=data['age'],
                        email=data['email']
                    )
                    print("Student ID:", student.id)
            except Exception as e:
                print("Object creation error: ", str(e))
    except Exception as e:
        print("Celery:", str(e))

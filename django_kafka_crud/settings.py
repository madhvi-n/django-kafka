"""
Django settings for django_kafka_crud project.

Generated by 'django-admin startproject' using Django 3.1.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2f^)dfb-*$#ez%5jmibj0n4t&(+_rlwcz1wa1qetf7gxm8)fyz'

DATABASE_NAME = 'students'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = '123456'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'allauth',
    'allauth.account',
    'rest_framework',
    'core',
    'students',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_kafka_crud.core.middleware.RateLimiterMiddleware'
]

ROOT_URLCONF = 'django_kafka_crud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_kafka_crud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'students',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'postgresql', # Referers to postgresql service in docker
        'PORT': 5432,
    }
}

# Set up Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092' # Refers to kafka service in docker
KAFKA_TOPIC = 'student-topic'

# Add Kafka producer configuration
# KAFKA_PRODUCER_CONFIG = {
#     'bootstrap_servers': KAFKA_BOOTSTRAP_SERVERS,
#     'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
# }
#
# # Add Kafka consumer configuration
# KAFKA_CONSUMER_CONFIG = {
#     'bootstrap_servers': KAFKA_BOOTSTRAP_SERVERS,
#     'value_deserializer': lambda v: json.loads(v.decode('utf-8')),
# }


# Caching with Redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}



# Authentication backend
AUTHENCATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Rate limiter
# REST_FRAMEWORK = {
#     'DEFAULT_THROTTLE_CLASSES': [
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.UserRateThrottle',
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '1/minute',
#         'user': '1/minute',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Celery configuration
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'db+postgresql://postgres:123456@postgresql/students'

CELERY_BEAT_SCHEDULE = {
    'process-kafka-messages': {
        'task': 'students.tasks.process_kafka_messages',
        'schedule': 60.0,  # 60 seconds (1 minute)
    }
}

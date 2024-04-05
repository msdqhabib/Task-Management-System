from pathlib import Path
import os


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'HOST': 'localhost',
        'PORT': '',
        'USER': 'ubuntu',
        'PASSWORD': 'ubuntu',
    }
}


# Logging Configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/home/ubuntu/Fulfillkaro-Portal/cron.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True,
        },
        "api_integration": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True,
        }
    },
}


ALLOWED_HOSTS = ['*']

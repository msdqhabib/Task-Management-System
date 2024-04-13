from pathlib import Path
import os


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': 'database-1.cd40gyq2y2ei.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}


# # Logging Configuration
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "file": {
#             "level": "INFO",
#             "class": "logging.FileHandler",
#             "filename": "/home/ubuntu/Task-Management-System/error.log",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file"],
#             "level": "INFO",
#             "propagate": True,
#         },
#         "api_integration": {
#             "handlers": ["file"],
#             "level": "INFO",
#             "propagate": True,
#         }
#     },
# }


ALLOWED_HOSTS = ['*']

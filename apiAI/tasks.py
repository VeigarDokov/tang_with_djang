"""string"""
from datetime import timedelta
from celery import shared_task
from .management.commands.update_api_data import Command


@shared_task
def update_data_task():
    """string"""
    Command().handle()


# settings.py
CELERY_BEAT_SCHEDULE = {
    'update_data_every_minute': {
        'task': 'apiAI.tasks.update_data_task',
        'schedule': timedelta(seconds=10),
    },
}

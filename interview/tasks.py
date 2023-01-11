from __future__ import absolute_import, unicode_literals

# start celery service: DJANGO_SETTINGS_MODULE=settings.local celery --app recruitment worker -l info
# start flower:  DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment flower --broker=redis://localhost:6379/0
from celery import shared_task
from .dingtalk import send

@shared_task
def send_dingtalk_message(message):
    send(message)
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from jobs.models import Job
from interview.dingtalk import send
import logging

logger = logging.getLogger(__name__)

@receiver(signal=post_save, sender=Job, dispatch_uid="job_post_save_dispatcher")
def post_save_callback(sender, instance=None, created=False, **kwargs):
    message = "Job position %s has been changed" % instance.job_name
    logger(message)
    send(message)

@receiver(signal=post_delete, sender=Job, dispatch_uid="job_post_delete_dispatcher")
def post_delete_callback(sender, instance=None, using=None, **kwargs):
    message = "Job position %s has been deleted" % instance.job_name
    logger(message)
    send(message)
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

JobTypes = [
    (0, "Technology"),
    (1, "Product"),
    (2, "Management"),
    (3, "Design")
]

Cities = [
    (0, "New York"),
    (1, "Chicago"),
    (2, "Boston"),
    (3, "Los Angeles")
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, verbose_name="Job Type", choices=JobTypes)
    job_name = models.CharField(max_length=250, blank=False, verbose_name="Job Name")
    job_city = models.SmallIntegerField(blank=False, verbose_name="Job City", choices=Cities)
    job_responsibility = models.TextField(max_length=1024, verbose_name="Job Responsibility")
    job_requirement = models.TextField(max_length=1024, verbose_name="Job Requirement")
    creator = models.ForeignKey(User, verbose_name="Creator", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name="Created Date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="Modified Date", default=datetime.now)

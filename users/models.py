from django.db import models
from datetime import datetime
from interview.models import DEGREE_TYPE
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    username = models.CharField(max_length=135, verbose_name="Name")
    applicant = models.ForeignKey(User, verbose_name="Applicant", null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name="City")
    phone = models.CharField(max_length=135, verbose_name="Phone")
    email = models.EmailField(max_length=135, blank=True, verbose_name="Email")
    apply_position = models.CharField(max_length=135, blank=True, verbose_name="Position")
    born_address = models.CharField(max_length=135, blank=True, verbose_name="Born Address")
    gender = models.CharField(max_length=135, blank=True, verbose_name="Gender")

    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name="Undergraduate School or College")
    master_school = models.CharField(max_length=135, blank=True, verbose_name="Graduate School or College")
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name="Phd School or College")
    bachelor_GPA = models.CharField(max_length=135, null=True, blank=True, verbose_name="Undergraduate GPA")
    master_GPA = models.CharField(max_length=135, null=True, blank=True, verbose_name="Graduate GPA")
    doctor_GPA = models.CharField(max_length=135, null=True, blank=True, verbose_name="Phd GPA")
    major = models.CharField(max_length=135, blank=True, verbose_name="Major")
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name="Degree")
    created_date = models.DateTimeField(verbose_name="Created Date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="Modified Date", default=datetime.now)

    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name="Introduction")
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name="Work Experience")
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name="Project Experience")

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume List"
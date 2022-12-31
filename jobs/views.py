from django.shortcuts import render
from jobs.models import Job

# Create your views here.
def joblist(request):
    job_list = Job.objects.order_by('job-type')

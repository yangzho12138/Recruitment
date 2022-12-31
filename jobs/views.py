from django.http import JsonResponse
from jobs.models import Job
from jobs.models import Cities, JobTypes


# Create your views here.

# get all the job
def joblist(request):
    job_list = Job.objects.order_by('job_type')

    data = []
    if job_list:
        for job in job_list:
            j = {}
            j['job_type'] = JobTypes[job.job_type][1]
            j['job_city'] = Cities[job.job_city][1]
            j['job_name'] = job.job_name
            j['job_responsibility'] = job.job_responsibility
            j['job_requirement'] = job.job_requirement
            # foreign key type: <class 'django.contrib.auth.models.User'> , can not be serializable, transfer to str
            j['creator'] = str(job.creator)
            j['created_date'] = job.created_date
            j['modified_date'] = job.modified_date
            data.append(j)

    return JsonResponse({
        'status': 200,
        'message': 'success',
        'data': data
    })



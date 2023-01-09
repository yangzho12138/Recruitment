from django.http import JsonResponse
from jobs.models import Job
from jobs.models import Cities, JobTypes

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class JobView(APIView):

    def get(self, request):
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

        return Response({
            'status': 200,
            'message': 'success',
            'data': data
        })


class JobsView(APIView):

    def get(self, request, job_id):
        try:
            job = Job.objects.get(pk=job_id)

            data = {}
            data['job_type'] = JobTypes[job.job_type][1]
            data['job_city'] = Cities[job.job_city][1]
            data['job_name'] = job.job_name
            data['job_responsibility'] = job.job_responsibility
            data['job_requirement'] = job.job_requirement
            data['creator'] = str(job.creator)
            data['created_date'] = job.created_date
            data['modified_date'] = job.modified_date
            return JsonResponse({
                'status': 200,
                'message': 'success',
                'data': data
            })

        except Job.DoesNotExist:
            return JsonResponse({
                'status': 404,
                'message': 'Job does not exist'
            })





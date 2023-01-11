from django.urls import re_path as url
from jobs.views import JobView, JobsView

from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    url(r'^api/jobs/joblist', JobView.as_view()),
    url(r'api/jobs/(?P<job_id>\d+)/$', JobsView.as_view()),
    path('sentry-debug/', trigger_error), # make a fault -> catched by sentry
]
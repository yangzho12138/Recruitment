from django.urls import re_path as url
from jobs.views import JobView, JobsView

urlpatterns = [
    url(r'^joblist/', JobView.as_view()),
    url(r'job/(?P<job_id>\d+)/$', JobsView.as_view())
]
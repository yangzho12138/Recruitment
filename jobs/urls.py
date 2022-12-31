from django.urls import re_path as url
from jobs import views

urlpatterns = [
    url(r'^joblist/', views.joblist),
    url(r'job/(?P<job_id>\d+)/$', views.jobdetail)
]
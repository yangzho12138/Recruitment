from django.urls import re_path as url
from django.urls import path
from users.views import UserView, InfoView, ResumeView, uploadFileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url(r'^api/users/resume/upload', uploadFileView.as_view()),
    url(r'^api/users/resume', ResumeView.as_view()),
    url(r'^api/users/register', UserView.as_view()),
    url(r'^api/users/getinfo', InfoView.as_view()),
    path('api/users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
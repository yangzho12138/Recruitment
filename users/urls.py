from django.urls import re_path as url
from django.urls import path
from users.views import UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url(r'^api/users/register', UserView.as_view()),
    path('api/users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
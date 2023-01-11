from django.urls import path
from interview import views

urlpatterns = [
    path('resume/<int:pk>/', views.ResumeDetailView.as_view()),
]
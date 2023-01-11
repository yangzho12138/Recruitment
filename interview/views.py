from django.shortcuts import render
from django.views.generic.detail import DetailView
from users.models import Resume

# Create your views here.
class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume_detail.html'

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from users.models import Resume
from interview.models import Candidate
from datetime import datetime
from django.contrib import messages

# Register your models here.

def enter_interview_process(modeladmin, request, queryset):
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        candidate.__dict__.update(resume.__dict__) # __dict__ -> all attributes
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = candidate.username + "," + candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, 'Candidate %s enter the interview!' % candidate_names) # message on webpage


class ResumeAdmin(admin.ModelAdmin):
    actions = (enter_interview_process, )

    list_display = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'doctor_school','major', 'created_date', 'attachment')
    readonly_fields = ('applicant', 'created_date', 'modified_date',)
    fieldsets = (
        (None, {'fields': ("applicant", ("username", "city", "phone"),("email", "apply_position", "born_address", "gender", ),("bachelor_school", "bachelor_GPA", "master_school", "master_GPA", "doctor_school", "doctor_GPA"), ("major", "degree"), ('created_date', 'modified_date'),"candidate_introduction", "work_experience" ,"project_experience",)}),
    )
    search_fields = ('username', 'email')
    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)


# User = get_user_model()

# admin.site.register(User, UserAdmin)
admin.site.register(Resume, ResumeAdmin)

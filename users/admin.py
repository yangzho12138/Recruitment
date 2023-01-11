from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from users.models import Resume

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'doctor_school','major', 'created_date')
    readonly_fields = ('applicant', 'created_date', 'modified_date',)
    fieldsets = (
        (None, {'fields': ("applicant", ("username", "city", "phone"),("email", "apply_position", "born_address", "gender", ),("bachelor_school", "bachelor_GPA", "master_school", "master_GPA", "doctor_school", "doctor_GPA"), ("major", "degree"), ('created_date', 'modified_date'),"candidate_introduction", "work_experience" ,"project_experience",)}),
    )
    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)

# User = get_user_model()

# admin.site.register(User, UserAdmin)
admin.site.register(Resume, ResumeAdmin)

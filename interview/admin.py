from django.contrib import admin
from interview.models import Candidate
from django.http import HttpResponse
import csv
from datetime import datetime
import logging
from interview.candidate_fieldset import default_fieldsets, default_fieldsets_first, default_fieldsets_second
from django.db.models import Q
from django.contrib import messages
from users.models import Resume
from django.utils.safestring import mark_safe
from .tasks import send_dingtalk_message
from jobs.producer import publish

# customize the log
logger = logging.getLogger(__name__)

# Register your models here.
exportable_fields = ('username', 'city', 'phone', 'bachelor_school', 'master_school', 'doctor_school', 'degree', 'first_result', 'first_interviewer_user',
                     'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')


# notify the interviewer
def notify_interviewer(modeladmin, request, queryset):
    candidates = ""
    interviewers = ""
    print(queryset)
    for obj in queryset:
        candidates = obj.username + ";" + candidates
        interviewers = obj.first_interviewer_user.username + ";" + interviewers
    # async task
    send_dingtalk_message.delay("Candidates %s, congratulations, you are in the intesrview phase, the interviewers are %s, please prepare the interview fully" % (candidates, interviewers))
    messages.add_message(request, messages.INFO,
                         'Send notification successfully')  # message on webpage

def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % ('recruitment-candidates', datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

    # csv header
    writer = csv.writer(response)
    writer.writerow(
        # use verbose name of each filed as the header of csv
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )

    # print(queryset)  <QuerySet [<Candidate: Yuan Su>, <Candidate: Zhiyuan Yu>, <Candidate: ﻿Yuankai Wang>, <Candidate: Yang Zhou>]>
    for obj in queryset:
        csv_line = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line.append(field_value)
        writer.writerow(csv_line)

    logger.info("%s exported %s records" % (request.user, len(queryset)))
    return response


def notify_hired(modeladmin, request, queryset):
    candidates = ""
    print(queryset)
    for obj in queryset:
        candidates = obj.username + ";" + candidates
        data = {
            'email': obj.email
        }
        publish("candidate hired", data)
    # async task
    send_dingtalk_message.delay("Candidates %s, congratulations, you get the offer!" % candidates)
    messages.add_message(request, messages.INFO,
                         'Send notification successfully')  # message on webpage


export_model_as_csv.allowed_permissions = ('export', )


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = (
        "username", "get_resume", "city", "first_score", "first_result", "first_interviewer_user",
        "second_result", "second_interviewer_user", "hr_score", "hr_result", "last_editor"
    )

    # has_[permission_name]_permission
    # Now, admin can add/cancel the permission in group part of the system
    def has_export_permission(self, request):
        opts = self.opts
        return request.user.has_perm('%s.%s' % (opts.app_label, "export"))

    # specify different authentication to different groups
    def get_group_name(self, user):
        group_name = []
        for g in user.groups.all():
            group_name.append(g.name)
        return group_name

    # built-in functions -> readonly-fields = ()
    def get_readonly_fields(self, request, obj):
        group_name = self.get_group_name(request.user)

        if 'interviewer' in group_name:
            logger.info("%s is in interviewer group" % request.user.username)
            return ("first_interviewer_user", "second_interviewer_user",)
        return ()

    # can be edit in the list page (a easier way to edit than go into the detail page)
    # not built-in function
    def get_list_editable(self, request):
        group_name = self.get_group_name(request.user)

        if 'hr' in group_name or request.user.is_superuser:
            return ("first_interviewer_user", "second_interviewer_user",)
        return ()

    # override list_editable
    def get_changelist_instance(self, request):
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)

    actions = (export_model_as_csv, notify_interviewer, notify_hired)

    # search function
    search_fields = ('username', 'phone', 'email', "bachelor_school", "master_school", "doctor_school")

    # filter function
    list_filter = ('city', 'first_result', 'second_result', 'hr_result', 'first_interviewer_user', 'second_interviewer_user', 'hr_interviewer_user')

    # showed in order
    ordering = ('hr_result', 'second_result', 'first_result')

    def get_resume(self, obj):
        if not obj.email:
            return ""
        resume = Resume.objects.filter(email=obj.email)
        if resume and len(resume) > 0:
            return mark_safe('<a href="/resume/%s" target="_blank"> %s </a>' % (resume[0].id, "Resume"))
        return ""
    # "get_resume" become a tag and can be displayed in the list_display
    get_resume.allow_tags = True

    # different roles can see different fieldsets
    def get_fieldsets(self, request, obj):
        group_name = self.get_group_name(request.user)

        if 'interviewer' in group_name and obj.first_interviewer_user == request.user and obj.second_interviewer_user != request.user:
            return default_fieldsets_first
        if 'interviewer' in group_name and obj.second_interviewer_user == request.user:
            return default_fieldsets_second
        return default_fieldsets

    # different roles can see different dataset (they can only see the relevant candidate in the list page)
    def get_queryset(self, request):
        qs = super(CandidateAdmin, self).get_queryset(request) # all dataset

        group_name = self.get_group_name(request.user)
        if request.user.is_superuser or 'hr' in group_name:
            return qs
        return Candidate.objects.filter(
            # database and/or operation
            Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user)
        )


admin.site.register(Candidate, CandidateAdmin)

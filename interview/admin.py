from django.contrib import admin
from interview.models import Candidate
from django.http import HttpResponse
import csv
from datetime import datetime
import logging

# customize the log
logger = logging.getLogger(__name__)

# Register your models here.
exportable_fields = ('username', 'city', 'phone', 'bachelor_school', 'master_school', 'doctor_school', 'degree', 'first_result', 'first_interviewer_user',
                     'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')

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


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = (
        "username", "city", "first_score", "first_result", "first_interviewer_user",
        "second_result", "second_interviewer_user", "hr_score", "hr_result", "last_editor"
    )

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
    # no built-in function
    def get_list_editable(self, request):
        group_name = self.get_group_name(request.user)

        if 'hr' in group_name or request.user.is_superuser:
            return ("first_interviewer_user", "second_interviewer_user",)
        return ()

    # override list_editable
    def get_changelist_instance(self, request):
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)


    actions = (export_model_as_csv, )

    # search function
    search_fields = ('username', 'phone', 'email', "bachelor_school", "master_school", "doctor_school")

    # filter function
    list_filter = ('city', 'first_result', 'second_result', 'hr_result', 'first_interviewer_user', 'second_interviewer_user', 'hr_interviewer_user')

    # showed in order
    ordering = ('hr_result', 'second_result', 'first_result')

    # show info with grouping
    # () several fields -> these fields will be shown in one line
    fieldsets = (
        (None, {'fields': ("userid", ("username", "city", "phone", "email"), ("apply_position", "address", "gender", "candidate_remark"), ("bachelor_school", "master_school", "doctor_school"), ("major", "degree"), ("test_score_of_general_ability", "test_score_of_professional_ability"), "last_editor")}),
        ('First Round Interview', {'fields': (("first_score", "first_learning_ability", "first_professional_competency"), "first_advantage", "first_disadvantage", ("first_result", "first_recommend_position", "first_interviewer_user", "first_remark"))}),
        ('Second Round Interview', {'fields': (("second_score", "second_learning_ability", "second_professional_competency", "second_pursue_of_excellence", "second_communication_ability", "second_pressure_score"), "second_advantage", "second_disadvantage", ("second_result", "second_recommend_position", "second_interviewer_user", "second_remark"))}),
        ('HR Interview', {'fields': (("hr_score", "hr_responsibility", "hr_communication_ability", "hr_logic_ability", "hr_potential", "hr_stability"), "hr_advantage", "hr_disadvantage", ("hr_result", "hr_interviewer_user", "hr_remark"))})
    )



admin.site.register(Candidate, CandidateAdmin)

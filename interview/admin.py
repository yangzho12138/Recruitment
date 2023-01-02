from django.contrib import admin
from interview.models import Candidate

# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = (
        "username", "city", "first_score", "first_result", "first_interviewer_user",
        "second_result", "second_interviewer_user", "hr_score", "hr_result", "last_editor"
    )

    # show info with grouping
    # () several fields -> these fields will be shown in one line
    fieldsets = (
        (None, {'fields': ("userid", ("username", "city", "phone", "email"), ("apply_position", "address", "gender", "candidate_remark"), ("bachelor_school", "master_school", "doctor_school"), ("major", "degree"), ("test_score_of_general_ability", "test_score_of_professional_ability"), "last_editor")}),
        ('First Round Interview', {'fields': (("first_score", "first_learning_ability", "first_professional_competency"), "first_advantage", "first_disadvantage", ("first_result", "first_recommend_position", "first_interviewer_user", "first_remark"))}),
        ('Second Round Interview', {'fields': (("second_score", "second_learning_ability", "second_professional_competency", "second_pursue_of_excellence", "second_communication_ability", "second_pressure_score"), "second_advantage", "second_disadvantage", ("second_result", "second_recommend_position", "second_interviewer_user", "second_remark"))}),
        ('HR Interview', {'fields': (("hr_score", "hr_responsibility", "hr_communication_ability", "hr_logic_ability", "hr_potential", "hr_stability"), "hr_advantage", "hr_disadvantage", ("hr_result", "hr_interviewer_user", "hr_remark"))})
    )

admin.site.register(Candidate, CandidateAdmin)
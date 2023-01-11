from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DEGREE_TYPE = (('Undergraduate', 'Undergraduate'), ('Graduate', 'Graduate'), ('Phd', 'Phd'))

FIRST_INTERVIEW_RESULT_TYPE = (('Recommended to next round', 'Recommended to next round'),
                               ('Waiting list', 'Waiting list'), ('Failed', 'Failed'))

INTERVIEW_RESULT_TYPE = (('Recommended to be hired', 'Recommended to be hired'),
                               ('Waiting list', 'Waiting list'), ('Failed', 'Failed'))

HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))

class Candidate(models.Model):
    # basic info
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name='Candidate ID')
    username = models.CharField(max_length=135, verbose_name='Candidate Name')
    city = models.CharField(max_length=135, verbose_name='City')
    phone = models.CharField(max_length=135, verbose_name='Phone')
    email = models.EmailField(max_length=135, blank=True, verbose_name='Email')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name='Applied Position')
    address = models.CharField(max_length=135, blank=True, verbose_name='Address')
    gender = models.CharField(max_length=135, blank=True, verbose_name='Gender')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name='Remark')

    # school and education level
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name='Undergraduate School or College')
    master_school = models.CharField(max_length=135, blank=True, verbose_name='Graduate School or College')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name='PHD School or College')
    bachelor_GPA = models.FloatField(null=True, blank=True, verbose_name="Undergraduate GPA")
    master_GPA = models.FloatField(null=True, blank=True, verbose_name="Graduate GPA")
    doctor_GPA = models.FloatField(null=True, blank=True, verbose_name="Phd GPA")
    major = models.CharField(max_length=135, blank=True, verbose_name='Major')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name='Education Level')

    # OA
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                                        verbose_name='General Test Score')
    test_score_of_professional_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                                             verbose_name='Professional Test Score')

    # first round interview
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                      verbose_name='First Round Score',
                                      help_text='Between1-5，Extraordinary: >=4.5，Excellent: 4-4.4，Good: 3.5-3.9，General: 3-3.4，Bad: <3')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name='Learning Ability Score')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                        verbose_name='Professional Ability Score')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name='Advantage')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='Disadvantage')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name='First Round Result')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name='Recommended Position')
    first_interviewer_user = models.ForeignKey(User, related_name='first_interviewer_user', blank=True, null=True,
                                               on_delete=models.CASCADE, verbose_name='First Round Interviewer')
    first_remark = models.CharField(max_length=135, blank=True, verbose_name='First Round Remark')

    # second round interview
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                       verbose_name='Second Round Score',
                                       help_text='Between1-5，Extraordinary: >=4.5，Excellent: 4-4.4，Good: 3.5-3.9，General: 3-3.4，Bad: <3')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name='Learning Ability Score')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                         verbose_name='Professional Ability Score')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                      verbose_name='Excellence Pursue Score')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                       verbose_name='Communication Ability Score')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                verbose_name='Under Pressure Score')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name='Advantage')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='Disadvantage')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name='Second Round Result')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name='Recommended Position')
    second_interviewer_user = models.ForeignKey(User, related_name='second_interviewer_user', blank=True, null=True,
                                                on_delete=models.CASCADE, verbose_name='Second Round Interviewer')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name='Second Round Remark')

    # HR interview
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR Score')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR Responsibility')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                                verbose_name='HR Communication Ability')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR Logic Ability')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR Potential')
    hr_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR Stability')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name='HR Advantage')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='HR Disadvantage')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name='HR Result')
    hr_interviewer_user = models.ForeignKey(User, related_name='hr_interviewer_user', blank=True, null=True,
                                            on_delete=models.CASCADE, verbose_name='HR Result')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name='HR Remark')

    creator = models.CharField(max_length=256, blank=True, verbose_name='Creator')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated Date')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name='Last Editor')

    class Meta:
        db_table = 'candidate'
        verbose_name = 'candidate'
        verbose_name_plural = 'candidates'
        # admin.py action permission
        permissions = [
            ("export", "Can export candidate list"),
            ("notify", "notify interviewer for candidate review"),
        ]

    # Python 2 transfer object to str, no __unicode__() -> use  __str__()
    def __unicode__(self):
        return self.username

    # Python 3 use __str__() directly
    def __str__(self):
        return self.username
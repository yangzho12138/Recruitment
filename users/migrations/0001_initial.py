# Generated by Django 4.1 on 2023-01-11 00:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=135, verbose_name="Name")),
                ("city", models.CharField(max_length=135, verbose_name="City")),
                ("phone", models.CharField(max_length=135, verbose_name="Phone")),
                (
                    "email",
                    models.EmailField(blank=True, max_length=135, verbose_name="Email"),
                ),
                (
                    "apply_position",
                    models.CharField(
                        blank=True, max_length=135, verbose_name="Position"
                    ),
                ),
                (
                    "born_address",
                    models.CharField(
                        blank=True, max_length=135, verbose_name="Born Address"
                    ),
                ),
                (
                    "gender",
                    models.CharField(blank=True, max_length=135, verbose_name="Gender"),
                ),
                (
                    "bachelor_school",
                    models.CharField(
                        blank=True,
                        max_length=135,
                        verbose_name="Undergraduate School or College",
                    ),
                ),
                (
                    "master_school",
                    models.CharField(
                        blank=True,
                        max_length=135,
                        verbose_name="Graduate School or College",
                    ),
                ),
                (
                    "doctor_school",
                    models.CharField(
                        blank=True, max_length=135, verbose_name="Phd School or College"
                    ),
                ),
                (
                    "bachelor_GPA",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Undergraduate GPA"
                    ),
                ),
                (
                    "master_GPA",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Graduate GPA"
                    ),
                ),
                (
                    "doctor_GPA",
                    models.FloatField(blank=True, null=True, verbose_name="Phd GPA"),
                ),
                (
                    "major",
                    models.CharField(blank=True, max_length=135, verbose_name="Major"),
                ),
                (
                    "degree",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Undergraduate", "Undergraduate"),
                            ("Graduate", "Graduate"),
                            ("Phd", "Phd"),
                        ],
                        max_length=135,
                        verbose_name="Degree",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="Created Date"
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="Modified Date"
                    ),
                ),
                (
                    "candidate_introduction",
                    models.TextField(
                        blank=True, max_length=1024, verbose_name="Introduction"
                    ),
                ),
                (
                    "work_experience",
                    models.TextField(
                        blank=True, max_length=1024, verbose_name="Work Experience"
                    ),
                ),
                (
                    "project_experience",
                    models.TextField(
                        blank=True, max_length=1024, verbose_name="Project Experience"
                    ),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Applicant",
                    ),
                ),
            ],
            options={"verbose_name": "Resume", "verbose_name_plural": "Resume List",},
        ),
    ]

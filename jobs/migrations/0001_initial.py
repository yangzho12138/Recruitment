# Generated by Django 4.1 on 2022-12-18 17:12

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
            name="Job",
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
                (
                    "job_type",
                    models.SmallIntegerField(
                        choices=[
                            (0, "technology"),
                            (1, "Product"),
                            (2, "Management"),
                            (3, "Design"),
                        ],
                        verbose_name="Job Type",
                    ),
                ),
                ("job_name", models.CharField(max_length=250, verbose_name="Job Name")),
                (
                    "job_city",
                    models.SmallIntegerField(
                        choices=[
                            (0, "New York"),
                            (1, "Chicago"),
                            (2, "Boston"),
                            (3, ""),
                        ],
                        verbose_name="Job City",
                    ),
                ),
                (
                    "job_responsibility",
                    models.TextField(
                        max_length=1024, verbose_name="Job Responsibility"
                    ),
                ),
                (
                    "job_requirement",
                    models.TextField(max_length=1024, verbose_name="Job Requirement"),
                ),
                ("cretaed_date", models.DateTimeField(verbose_name="Created Date")),
                ("modified_date", models.DateTimeField(verbose_name="Modified Date")),
                (
                    "creator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
            ],
        ),
    ]

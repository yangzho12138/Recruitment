# Generated by Django 4.1 on 2023-01-11 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0004_alter_resume_options"),
    ]

    operations = [
        migrations.DeleteModel(name="Resume",),
    ]

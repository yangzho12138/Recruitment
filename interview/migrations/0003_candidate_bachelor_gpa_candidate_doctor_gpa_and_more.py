# Generated by Django 4.1 on 2023-01-10 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interview", "0002_alter_candidate_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="bachelor_GPA",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Undergraduate GPA"
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="doctor_GPA",
            field=models.FloatField(blank=True, null=True, verbose_name="Phd GPA"),
        ),
        migrations.AddField(
            model_name="candidate",
            name="master_GPA",
            field=models.FloatField(blank=True, null=True, verbose_name="Graduate GPA"),
        ),
    ]
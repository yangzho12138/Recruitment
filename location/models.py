# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=20)
    country_code = models.CharField(unique=True, max_length=2)
    dial_code = models.CharField(max_length=5)
    currency_name = models.CharField(max_length=20)
    currency_symbol = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    currency_code = models.CharField(max_length=10)
    country_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'

    def __str__(self):
        return self.country_name if self.country_name else ""


class States(models.Model):
    id_state = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    country_id = models.ForeignKey(Countries, db_column='country_id', blank=True, null=True, on_delete=models.SET_NULL)
    is_active = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    lang = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'

    def __str__(self):
        return self.state if self.state else ""


class Cities(models.Model):
    id_city = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=30)
    state_id = models.ForeignKey(States, db_column='state_id', blank=True, null=True, on_delete=models.SET_NULL)
    is_default = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    sort_order = models.IntegerField()
    lang = models.CharField(max_length=10)
    created_at = models.CharField(max_length=10)
    updated_at = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'

    def __str__(self):
        return self.city if self.city else ""

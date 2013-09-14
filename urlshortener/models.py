# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Urls(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=11L, unique=True, blank=True)
    long_url = models.CharField(max_length=150L, blank=True)
    created_at = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'urls'

class UrlMetrics(models.Model):
    id = models.IntegerField(primary_key=True)
    clicks = models.IntegerField(null=True, blank=True)
    url = models.ForeignKey(Urls, null=True, blank=True)
    class Meta:
        db_table = 'url_metrics'
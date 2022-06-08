# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import jsonfield


class PerevalAdded(models.Model):
    date_added = models.DateTimeField(blank=False, null=False)
    raw_data = jsonfield.JSONField()
    images = jsonfield.JSONField()

    class Meta:
        db_table = 'pereval_added'


class PerevalAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_parent = models.BigIntegerField(null=False)
    title = models.TextField()
    STATUS_TYPES = {
        (1, 'new'),
        (2, 'pending'),
        (3, 'accepted'),
        (4, 'rejected'),
    }
    status = models.TextField(default='new', choices=STATUS_TYPES)

    class Meta:
        db_table = 'pereval_areas'


class PerevalImages(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField(null=False)

    class Meta:
        db_table = 'pereval_images'


class SprActivitiesTypes(models.Model):
    title = models.TextField()

    class Meta:
        db_table = 'spr_activities_types'

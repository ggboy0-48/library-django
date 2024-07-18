from django.db import models

# Create your models here.
class user(models.Model):
    id = models.BigIntegerField('主键',primary_key=True)

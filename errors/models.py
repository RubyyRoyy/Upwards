from django.db import models


# Create your models here.
class Error(models.Model):
    error = models.TextField()
    status_code = models.IntegerField()

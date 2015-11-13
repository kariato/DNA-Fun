from django.db import models
from django.contrib.auth.models import import User

# Create your models here.
class DNASegment(models.Model):
    user = models
    chromosome = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()
    cm = models.IntegerField()


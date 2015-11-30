from django.db import models
from django.contrib.auth.models import User

class DNAKits(models.Model):
    user = models.ForeignKey(User, related_name="DNAMatches_user")
    resultSet = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    def __str__(self):
        return "{0} ({1})".format(self.name,self.resultSet)

class DNAMatches(models.Model):
    resultSet = models.ForeignKey(DNAKits)
    fullName = models.CharField(max_length=300)
    firstName = models.CharField(max_length=300)
    middleName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=300)
    matchDate = models.DateField()
    relationshipRange = models.CharField(max_length=300)
    suggestedRelationship = models.CharField(max_length=300)
    sharedCM = models.FloatField()
    longestBlock = models.FloatField()
    knownRelationship = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    ancestralSurnames = models.CharField(max_length=3000)

# Create your models here.
class DNASegment(models.Model):
    matchname = models.ForeignKey(DNAMatches)
    chromosome = models.IntegerField()
    startLocation = models.IntegerField()
    endLocation = models.IntegerField()
    centimorgans = models.FloatField()
    matchingSnps = models.FloatField()



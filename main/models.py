from django.db import models

# Create your models here.

class Representative(models.Model):
    sex = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
    lastname = models.CharField(max_length=300, blank=True)
    party = models.CharField(max_length=300, blank=True)
    election_type = models.CharField(max_length=300, blank=True)
    entity = models.CharField(max_length=300, blank=True)
    district = models.CharField(max_length=300, blank=True)
    circunscription = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=300, blank=True)
    extension = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    commissions = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    patrimony = models.CharField(max_length=300, blank=True)
    answer = models.CharField(max_length=300, blank=True)
    answer_why = models.TextField(blank=True)
    suplent = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=300, blank=True)

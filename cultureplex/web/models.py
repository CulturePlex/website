from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    active = models.BooleanField()

class Publication(models.Model):
    authors = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year =  models.IntegerField(max_length=4)
    publication_type = models.CharField(max_length=200)
    pdf = models.CharField(max_length=200)

class People(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    blog = models.CharField(max_length=200)
    social = models.CharField(max_length=200)


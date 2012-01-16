from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    active = models.BooleanField()
    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    blog = models.CharField(max_length=200)
    social = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Publication(models.Model):
    PUB_TYPES = (
        (u'CG', u'Congreso'),
        (u'CF', u'Conferencia'),
        (u'W', u'Workshop'),
    )
    external_authors = models.CharField(max_length=200)
    internal_authors = models.ForeignKey(Person)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    publication_type = models.CharField(max_length=200, choices=PUB_TYPES)
    pdf = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title

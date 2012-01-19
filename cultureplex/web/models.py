from django.db import models

class Person(models.Model):
    POSITION_TYPES = (
        (u'F', u'Faculty'),
        (u'S', u'Staff'),
        (u'P', u'PhD'),
        (u'ST', u'Student'),
        (u'US', u'Undergraduate Student'),
        (u'P', u'Collaborator'),
        (U'A', u'Alumnus/a')
    )
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,blank=True)
    mobile = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200)
    bio = models.TextField(max_length=2000)
    blog = models.CharField(max_length=200,blank=True)
    twitter = models.CharField(max_length=200,blank=True)
    github = models.CharField(max_length=200,blank=True)
    facebook = models.CharField(max_length=200,blank=True)
    googleplus = models.CharField(max_length=200,blank=True)
    position = models.CharField(max_length=200, choices=POSITION_TYPES)
    image = models.ImageField(upload_to='persons_images',blank=True)
    active = models.BooleanField()
    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    contact = models.ForeignKey(Person)
    members = models.ManyToManyField(Person,related_name='+')
    description = models.TextField(max_length=2000)
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects_images',blank=True)
    active = models.BooleanField()
    incarousel = models.BooleanField()
    def __unicode__(self):
        return self.name

class Publication(models.Model):
    PUB_TYPES = (
        (u'Pa', u'Paper'),
        (u'PhDT', u'PhD Thesis'),
        (u'MsT', u'Ms Thesis'),
        (u'Talk', u'Talk'),
        (u'Present', u'Presentation'),
        (u'Book', u'Book'),
        (u'Chapter', u'Chapter Book'),
        (u'Procceding', u'Procceding'),
    )
    authors = models.ManyToManyField(Person,related_name='-')
    aceptation_date = models.DateField(blank=True)
    publication_date = models.DateField(blank=True)
    related_projects = models.ManyToManyField(Project,related_name='-',blank=True)
    abstract = models.TextField(max_length=2000)
    keywords = models.TextField(max_length=2000,blank=True)
    title = models.CharField(max_length=200)
    hosted_at = models.CharField(max_length=200,blank=True)
    url_hosted_at = models.CharField(max_length=200,blank=True)
    publication_type = models.CharField(max_length=200, choices=PUB_TYPES)
    document = models.FileField(upload_to='publications')
    def __unicode__(self):
        return self.title

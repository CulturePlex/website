from django.db import models

class Person(models.Model):
    POSITION_TYPES = (
        (u'Faculty', u'Faculty'),
        (u'Staff', u'Staff'),
        (u'PhD', u'PhD'),
        (u'Student', u'Student'),
        (u'Undergraduate Student', u'Undergraduate Student'),
        (u'Collaborator', u'Collaborator'),
        (U'Alumnus/a', u'Alumnus/a')
    )
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,blank=True)
    mobile = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200)
    bio = models.TextField(max_length=2000)
    blog = models.URLField(verify_exists=False,max_length=200,blank=True)
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
    url = models.URLField(verify_exists=False,max_length=200)
    image = models.ImageField(upload_to='projects_images',blank=True)
    active = models.BooleanField()
    incarousel = models.BooleanField()
    def __unicode__(self):
        return self.name

class Publication(models.Model):
    PUB_TYPES = (
        (u'Paper', u'Paper'),
        (u'PhD Thesis', u'PhD Thesis'),
        (u'Ms Thesis', u'Ms Thesis'),
        (u'Talk', u'Talk'),
        (u'Presentation', u'Presentation'),
        (u'Book', u'Book'),
        (u'Chapter Book', u'Chapter Book'),
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
    url_hosted_at = models.URLField(verify_exists=False,max_length=200,blank=True)
    publication_type = models.CharField(max_length=200, choices=PUB_TYPES)
    document = models.FileField(upload_to='publications')
    def __unicode__(self):
        return self.title

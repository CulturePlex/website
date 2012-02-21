from os import path
from StringIO import StringIO
from PIL import Image as PILImage

from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from fiber.models import Image

from web.fields import AutoSlugField


class Person(models.Model):
    POSITION_TYPES = (
        (u'Faculty', u'Faculty'),
        (u'Staff', u'Staff'),
        (u'PhD Student', u'PhD Student'),
        (u'MA Student', u'MA Student'),
        (u'Undergraduate Student', u'Undergraduate Student'),
        (u'Collaborator', u'Collaborator'),
        (U'Alumnus/a', u'Alumnus/a')
    )
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True)
    mobile = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200)
    bio = models.TextField(max_length=2000)
    blog = models.URLField(verify_exists=False, max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    github = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    googleplus = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=200, choices=POSITION_TYPES)
    image = models.ImageField(upload_to='persons_images', blank=True)
    active = models.BooleanField()
    slug = AutoSlugField(populate_from=['name'], max_length=100,
                         editable=False)

    @models.permalink
    def get_absolute_url(self):
        return ('web.views.person', [str(self.slug)])

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    contact = models.ForeignKey(Person)
    members = models.ManyToManyField(Person, related_name='+')
    description = models.TextField(max_length=2000)
    url = models.URLField(verify_exists=False, max_length=200)
    image = models.ImageField(upload_to='projects_images', blank=True)
    active = models.BooleanField()
    incarousel = models.BooleanField()
    slug = AutoSlugField(populate_from=['name'], max_length=100,
                         editable=False)

    @models.permalink
    def get_absolute_url(self):
        return ('web.views.project', [str(self.slug)])

    def __unicode__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=200)
    PUB_TYPES = (
        (u'Article', u'Article'),
        (u'Paper', u'Paper'),
        (u'PhD Thesis', u'PhD Thesis'),
        (u'Ms Thesis', u'Ms Thesis'),
        (u'Talk', u'Talk'),
        (u'Presentation', u'Presentation'),
        (u'Book', u'Book'),
        (u'Book Chapter', u'Book Chapter'),
        (u'Procceding', u'Procceding'),
    )
    authors = models.ManyToManyField(Person, related_name='-')
    aceptation_date = models.DateField(default=None, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    related_projects = models.ManyToManyField(Project, related_name='-',
                                              blank=True)
    abstract = models.TextField(max_length=2000)
    keywords = models.TextField(max_length=2000, blank=True)
    hosted_at = models.CharField(max_length=200, blank=True)
    url_hosted_at = models.URLField(verify_exists=False, max_length=200,
                                    blank=True)
    publication_type = models.CharField(max_length=200, choices=PUB_TYPES)
    document = models.FileField(upload_to='publications')
    slug = AutoSlugField(populate_from=['title'], max_length=100,
                         editable=False)

    @models.permalink
    def get_absolute_url(self):
        return ('web.views.publication', [str(self.slug)])

    def __unicode__(self):
        return self.title


@receiver(post_save, sender=Image)
def resize_as_a_new_fiber_image(*args, **kwargs):
    im = kwargs.get("instance", None)
    max_width = 450
    max_height = 300
    if im.image.width > max_width or im.image.height > max_height:
        size = (max_width, max_height)
        image = PILImage.open(im.image.path)
        xxx, image_name = path.split(im.image.path)
        if "." in image_name:
            image_name, extenstion = image_name.rsplit('.', 1)
            name = "%s_cropped.%s" % (image_name, extenstion)
        else:
            name = "%s_cropped" % image_name
        format = image.format
        if image.mode not in ("L", "RGB"):
            image = image.convert("RGB")
        resized_image = image.copy()
        resized_image.thumbnail(size, PILImage.ANTIALIAS)
        fp = StringIO()
        resized_image.save(fp, format, quality=128)
        cf = ContentFile(fp.getvalue())
        fiber_image = Image(title=im.title)
        fiber_image.image.save(name=name, content=cf, save=False)
        fiber_image.save()

from web.models import Project
from web.models import Publication
from web.models import Person
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','position','active')
    list_filter = ('active', 'position')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','contact','active','incarousel')
    list_filter = ('active', 'contact', 'incarousel')

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title','aceptation_date','publication_type')
    list_filter = ('publication_type',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Person, PersonAdmin)



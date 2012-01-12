from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Cultureplex:
     url(r'^$', 'web.views.index'),

    #Projects:
    url(r'^projects/$', 'web.views.projects'),
    url(r'^projects/(?P<project_id>\d+)/$', 'web.views.project'),

    #Publications:
    url(r'^publications/$', 'web.views.publications'),
    url(r'^publications/(?P<publication_id>\d+)/$', 'web.views.publication'),

    #People:
    url(r'^people/$', 'web.views.people_index'),
    url(r'^people/(?P<people_id>\d+)/$', 'web.views.people'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

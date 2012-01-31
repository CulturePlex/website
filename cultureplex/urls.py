from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.index'),
    # url(r'^cultureplex/', include('cultureplex.foo.urls')),

    #Projects:
    url(r'^projects/$', 'web.views.projects'),
    url(r'^projects/(?P<project_id>\d+)/$', 'web.views.project'),

    #Publications:
    url(r'^publications/$', 'web.views.publications'),
    url(r'^publications/(?P<publication_id>\d+)/$', 'web.views.publication'),

    #People:
    url(r'^persons/$', 'web.views.persons'),
    url(r'^persons/(?P<person_id>\d+)/$', 'web.views.person'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

    #Fiber:
    url(r'^api/v1/', include('fiber.api.urls')),
    url(r'^admin/fiber/', include('fiber.admin_urls')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
    url(r'', 'fiber.views.page')



)
if settings.DEBUG: 
    urlpatterns += patterns('', 
                    (r'^media/(?P<path>.*)$', 
'django.views.static.serve', {'document_root':'./media/'}), 
                    ) 

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

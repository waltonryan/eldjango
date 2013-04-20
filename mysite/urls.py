from django.conf.urls import patterns, include, url
from mysite.views import *
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Main Pages
	url(r'^$', 'mysite.views.home', name='home'),
	url(r'^rsvp/$', 'mysite.views.rsvp', name='rsvp'),
	url(r'^search/$', 'mysite.views.search', name='search'),
	url(r'^contact/$', 'mysite.views.contact', name='contact'),
	url(r'^userform/$', 'mysite.views.userform', name='userform'),
	
	# django-userena Pages
	(r'^accounts/', include('userena.urls')),

    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
					   
)

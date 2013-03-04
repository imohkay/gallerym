from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maskara.views.home', name='home'),
    # url(r'^maskara/', include('maskara.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple', 
    url(r'^$', 'direct_to_template', {'template': 'index.html'}),
    url(r'^artists$', 'direct_to_template', {'template': 'artists.html'}),
    url(r'^artist$', 'direct_to_template', {'template': 'artist.html'}),
    url(r'^exhibitions/current$', 'direct_to_template', {'template': 'exhibitions-current.html'}),
    url(r'^exhibitions/upcoming$', 'direct_to_template', {'template': 'exhibitions-upcoming.html'}),
    url(r'^exhibitions/previous$', 'direct_to_template', {'template': 'exhibitions-previous.html'}),
    url(r'^exhibition$', 'direct_to_template', {'template': 'exhibition.html'}),
    url(r'^events/current$', 'direct_to_template', {'template': 'events-current.html'}),
    url(r'^events/upcoming$', 'direct_to_template', {'template': 'events-upcoming.html'}),
    url(r'^events/previous$', 'direct_to_template', {'template': 'events-previous.html'}),
    url(r'^event$', 'direct_to_template', {'template': 'events.html'}),
    url(r'^contact$', 'direct_to_template', {'template': 'contact.html'}),
    url(r'^selected$', 'direct_to_template', {'template': 'selected.html'}),
)
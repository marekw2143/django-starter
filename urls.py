from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^', include('marekw2143_registration.urls')),
    url(r'^captcha/', include('captcha.urls')), #django-simple-captcha support

    # Examples:
    # url(r'^$', 'statser.views.home', name='home'),
    # url(r'^statser/', include('statser.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )

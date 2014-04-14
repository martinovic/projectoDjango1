from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from smarturls import surl
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    surl('/', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^contactos/', include('contactos.urls')),
    surl('/contactos/append_contacto/', 'contactos.views.append_contacto'),
    surl('/contactos/save_contactos/', 'contactos.views.save_contactos'),
    surl('/contactos/delete_contacto/', 'contactos.views.delete_contacto'),
    #surl('/polls/', include('polls.urls')),
    #surl('/polls/', include('polls.urls', namespace="polls")),
)

handler404 = 'mysite.views.handler404'
urlpatterns += staticfiles_urlpatterns()
from django.conf.urls import patterns
from smarturls import surl
from contactos import views


urlpatterns = patterns('',
    surl('^$', views.index, name='index'))

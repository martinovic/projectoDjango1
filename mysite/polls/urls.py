from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detalle, name="detalle"),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name="results"),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name="vote"),

)
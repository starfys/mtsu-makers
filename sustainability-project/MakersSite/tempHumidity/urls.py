from django.conf.urls import patterns, url
from . import views
#TEMPHUMIDITY URL
urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^submit$', views.submit, name='submit'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
)

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^register/$', views.register, name='register'),
        
        #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
)

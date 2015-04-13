from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^userInfo/', include('userInfo.urls')),
	url(r'^tempHumidity/', include('tempHumidity.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'MakersSite.views.home', name='HomePage.html'),
]

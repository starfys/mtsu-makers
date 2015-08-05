from django.conf.urls import include, url
from django.contrib import admin
from MakersSite import views

urlpatterns = [
	url(r'^userInfo/', include('userInfo.urls')),
	url(r'^tempHumidity/', include('tempHumidity.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'MakersSite.views.index'),
	#url(r'^partList/', include('partList.urls')),
	#url(r'^ongoingProjects/', include('ongoingProjects.urls'))
]

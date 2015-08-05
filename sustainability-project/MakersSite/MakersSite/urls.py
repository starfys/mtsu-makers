from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
	#url(r'^blog/', include('blog.urls')),
	#url(r'^userInfo/', include('userInfo.urls')),
  	url(r'^$', 'MakersSite.views.index'),
	url(r'^tempHumidity/',include('tempHumidity.urls')),
	url(r'^admin/', include(admin.site.urls)),
	#url(r'^partList/', include('partList.urls')),
	#url(r'^ongoingProjects/', include('ongoingProjects.urls'))
]

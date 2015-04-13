from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'MakersSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^userInfo/', include('userInfo.urls')),
	url(r'^tempHumidity/', include('tempHumidity.urls')),
	url(r'^admin/', include(admin.site.urls)),
]

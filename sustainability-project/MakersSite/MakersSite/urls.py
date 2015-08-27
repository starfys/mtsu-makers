from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
	#url(r'^blog/', include('blog.urls')),
	url(r'^userInfo/', include('userInfo.urls', namespace='userInfo'), name= 'userIno'),
  	url(r'^$', 'MakersSite.views.index',  name='MakersSite'),
	url(r'^tempHumidity/',include('tempHumidity.urls', namespace='tempHumidity'), name='tempHumidity'),
	url(r'^admin/', include(admin.site.urls)),
	#https://docs.djangoproject.com/en/1.4/howto/static-files/#staticfiles-development
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
	#url(r'^partList/', include('partList.urls')),
	#url(r'^ongoingProjects/', include('ongoingProjects.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

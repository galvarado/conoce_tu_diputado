from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('main.views',
    # Urls to main app
    url(r'^$', 'index', name='index'),
    url(r'^map/?$', 'map', name='map'),
    url(r'^map/get_deputies/?$', 'get_deputies', name='get_deputies'),
    url(r'^search/?$', 'search', name='search'),
    url(r'^search/get_deputies$', 'get_deputies_search', name='get_deputies_search'),
    url(r'^detail/(?P<id>\d+)/$', 'detail', name='detail'),
    # Urls to django admin
    url(r'^admin/', include(admin.site.urls)),
)

# Static files serve
from django.conf.urls.static import static
from django.conf import settings
import re

urlpatterns += patterns('',
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), 'django.contrib.staticfiles.views.serve', kwargs={'insecure':True}),
)
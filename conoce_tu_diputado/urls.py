from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
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
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photoflow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/admin/', include(admin.site.urls)),
    url(r'^api/markdown/', include( 'django_markdown.urls')),
    url(r'^api/blog/',include('blog.urls')),
    url(r'^api/picture/',include('picture.urls')),
    url(r'^api/website/',include('website.urls')),
)
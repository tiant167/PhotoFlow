from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
    url(r'^list/',BlogList.as_view()),
    url(r'^article/(?P<pk>\d+)/',BlogDetail.as_view())
)
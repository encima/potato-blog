from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'potato.views.home', name='home'),
    # url('', include('django.contrib.auth.urls')),
    url(r'^blog/', include('blog.urls')),

)

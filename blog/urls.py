from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new/', views.new_post, name='new_blog_post'),
    url(r'^view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
    url(r'^tag/(?P<slug>[^\.]+).html', views.view_tag, name='view_blog_category'),
)
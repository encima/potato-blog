from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login', 'django.contrib.auth.views.login'),
    url(r'^new/', views.new_post, name='new_blog_post'),
    url(r'^logout', views.user_logout),
    url(r'^edit/(?P<slug>[^\.]+)', views.edit_post, name='new_blog_post'),
    url(r'^delete/(?P<slug>[^\.]+)', views.delete_post, name='new_blog_post'),
    url(r'^view/(?P<slug>[^\.]+)', views.view_post, name='view_blog_post'),
)
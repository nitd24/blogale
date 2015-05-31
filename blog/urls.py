from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       #url(r'^aa(?P<article_id>\d+)/$', views.description, name='description'),

                       #url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<article_id>\d+)/$', views.description, name='description'),

                       url(r'^search/$', views.search, name='search')
)

handler404 = 'blog.views.error404'
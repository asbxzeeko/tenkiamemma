from django.conf.urls import url, patterns
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^drafts/', views.drafts, name='drafts'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.publish, name='publish'),
]
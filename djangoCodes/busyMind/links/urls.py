from django.conf.urls import url

from . import views

app_name = 'links'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
        #ex: /polls/5
        url(r'^(?P<pk>[a-zA-Z]+)/$', views.TopicView.as_view(), name='topic_view'),
        #ex: /polls/5/results
        url(r'^(?P<pk>[a-zA-Z]+)/link_itself/$', views.LinkItselfView.as_view(), name='link_itself'),
        #ex: /polls/5/vote
        url(r'^(?P<topic>[a-zA-Z]+)/view_links/$', views.view_links, name='view_links'),
]

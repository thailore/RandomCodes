from django.conf.urls import url

from . import views

app_name = 'memCall'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        #ex: /polls/5
        url(r'^(?P<pk>[a-zA-Z]+)/$', views.TopicView.as_view(), name='topic_view'),
        #ex: /polls/5/results
        url(r'^(?P<pk>[a-zA-Z]+)/link_itself/$', views.LinkItselfView.as_view(), name='link_itself'),
        #ex: /polls/5/vote
        url(r'^(?P<topic>[a-zA-Z]+)/view_links/$', views.view_links, name='view_links'),
	url(r'^add_topic/$', views.add_topic, name='add_topic'),
	url(r'^add_link/$', views.add_link, name='add_link'),
        url(r'^(?P<pk>[a-zA-Z]+)/delete_topic/$', views.delete_topic, name='delete_topic'),
        #url(r'^(?P<pk>[a-zA-Z]+)/delete_link/$', views.delete_link, name='delete_link'),
	
]

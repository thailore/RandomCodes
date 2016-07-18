"""busyMind URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^memCall/', include('memCall.urls')),
	url(r'^admin/', admin.site.urls),
]

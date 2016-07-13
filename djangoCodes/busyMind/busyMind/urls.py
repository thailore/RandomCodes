"""busyMind URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^memoryLoss/', include('memoryLoss.urls')),
	url(r'^admin/', admin.site.urls),
]

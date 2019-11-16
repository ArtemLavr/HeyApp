from django.urls import path
from django.conf.urls import url

from .views import index, devices, reconf
urlpatterns = [
	path('', index),
	path('devices', devices),
	url(r'reconf', reconf)
]
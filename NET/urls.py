from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView

from .views import index, devices, reconf,  snmp
urlpatterns = [
	path('', index, name='index'),
	path('devices', devices, name='devices'),
	path('snmp', snmp, name='snmp'),
	url(r'^zabbix/$', RedirectView.as_view(url='http://127.0.0.1:80'),
        name='zabbix'),
	url(r'reconf', reconf)

]
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView
from .utils.tftp_serv import tftp_run
import threading

from .views import index, devices, reconf,  snmp, login, set_snmp
urlpatterns = [
	path('', index, name='index'),
	path('devices', devices, name='devices'),
	path('snmp', snmp, name='snmp'),
	path('login',login, name='login'),
	url(r'^zabbix/$', RedirectView.as_view(url='http://127.0.0.1:80'),
        name='zabbix'),
	url(r'reconf', reconf),
	url(r'set_snmp', set_snmp)

]

x = threading.Thread(target = tftp_run)
x.start()
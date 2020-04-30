from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView
from .utils.tftp_serv import tftp_run
import threading

from .views import index, devices, snmp, login, set_snmp, netflow_setting
from .views import save_conf, set_conf, restore_os, reset_pass

urlpatterns = [
	path('', index, name='index'),
	path('devices', devices, name='devices'),
	path('snmp', snmp, name='snmp'),
	path('netflow_setting', netflow_setting, name='netflow_setting'),
	path('login',login, name='login'),
	url(r'^zabbix/$', RedirectView.as_view(url='http://127.0.0.1:80'), name='zabbix'),
	url(r'^netflow/$', RedirectView.as_view(url='http://127.0.0.1:3000'), name='netflow'),
	url(r'^ssh_telnet/$', RedirectView.as_view(url='http://127.0.0.1:8182'), name='ssh_telnet'),
	url(r'save_conf', save_conf),
	url(r'set_conf', set_conf),
	url(r'set_snmp', set_snmp),
	url(r'reset_pass', reset_pass),
	url(r'restore_os', restore_os),
	

]

x = threading.Thread(target = tftp_run)
x.start()
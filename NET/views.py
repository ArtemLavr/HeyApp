from django.shortcuts import render, redirect
from .utils.utils import Configure, SnmpSet, Get_Data
from subprocess import run,PIPE
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader 
from .models import Events, Nodes




def login(request):
	return render(
		request, 
		'login.html',
		)


def index(request):
	
	evs = Events.objects.order_by('-ev_time')
	nds = Nodes.objects.order_by('pk')
	metrics = Get_Data()
	print("METRICS:::")
	print(metrics.metric_list)
	context = {	'metrics': metrics.metric_list,
				'evs':evs,
				'nds':nds,
				}
	return render(
		request, 
		'index.html', context,
		)




def snmp(request):
	return render(
		request, 
		'snmptraps_setting.html',
		)

def netflow_setting (request):
	return render(
		request, 
		'netflow_setting.html',
		)


def devices(request):
	return render(
		request, 
		'devices.html', 
		)


def set_snmp(request):
	CONNECTION_TYPE = request.POST.get('connectMethod')
	USER_NAME = request.POST.get('username')
	PASSWORD = request.POST.get('PASSWORD') 
	DEVICES_IP = request.POST.get('DEVICES_IP')
	EN_PASS = request.POST.get('EN_PASS')
	SNMP_SERVER = request.POST.get('SNMP_SERVER')

	try:
		do_restore = SnmpSet(CONNECTION_TYPE, USER_NAME, PASSWORD, DEVICES_IP, EN_PASS, SNMP_SERVER)
		return redirect('snmp')
	except Exception as e:
		raise e

def set_netflow(request):
	CONNECTION_TYPE = request.POST.get('connectMethod')
	USER_NAME = request.POST.get('username')
	PASSWORD = request.POST.get('PASSWORD') 
	DEVICES_IP = request.POST.get('DEVICES_IP')
	EN_PASS = request.POST.get('EN_PASS')
	SNMP_SERVER = request.POST.get('SNMP_SERVER')

	try:
		do_restore = SnmpSet(CONNECTION_TYPE, USER_NAME, PASSWORD, DEVICES_IP, EN_PASS, SNMP_SERVER)
		return redirect('snmp')
	except Exception as e:
		raise e


def save_conf(request):
	print(request.POST)
	USER_NAME = request.POST.get('USER_NAME')

	PASSWORD = ''.join(request.POST.getlist('PASSWORD')).split()[0]
	SERVER_IP = ''.join(request.POST.getlist('SERVER_IP')).split()[0]
	DEVICES_IP = ''.join(request.POST.getlist('DEVICES_IP')).split()[0]
	EN_PASS = ''.join(request.POST.getlist('EN_PASS')).split()[0]
	CONF_NAME = ''.join(request.POST.getlist('CONF_NAME')).split()[0]
	
	if 'telnet_save' in request.POST:

		CONNECTION_TYPE = 'telnet'
		
		try:
			
			do_restore = Configure('Save',CONNECTION_TYPE, USER_NAME, PASSWORD, SERVER_IP, DEVICES_IP, EN_PASS, CONF_NAME)
			
			return redirect('devices')
		except Exception as e:
			raise e
			return redirect('devices')
	elif 'ssh_save' in request.POST:
		CONNECTION_TYPE = 'ssh'
	
		try:
			do_restore = Configure('Save',CONNECTION_TYPE, USER_NAME, PASSWORD, SERVER_IP, DEVICES_IP, EN_PASS, CONF_NAME)
			return redirect('devices')

		except Exception as e:
			raise e
		
def set_conf(request):
	print(request.POST)
	USER_NAME = request.POST.get('USER_NAME')
	PASSWORD = ''.join(request.POST.getlist('PASSWORD')).split()[0]
	SERVER_IP = ''.join(request.POST.getlist('SERVER_IP')).split()[0]
	DEVICES_IP = ''.join(request.POST.getlist('DEVICES_IP')).split()[0]
	EN_PASS = ''.join(request.POST.getlist('EN_PASS')).split()[0]
	CONF_NAME = ''.join(request.POST.getlist('CONF_NAME')).split()[0]
	
	if 'telnet_set' in request.POST:

		CONNECTION_TYPE = 'telnet'
		
		try:
			
			do_restore = Configure('Set',CONNECTION_TYPE, USER_NAME, PASSWORD, SERVER_IP, DEVICES_IP, EN_PASS, CONF_NAME)
			
			return redirect('devices')
		except Exception as e:
			raise e
			return redirect('devices')
	elif 'ssh_set' in request.POST:
		CONNECTION_TYPE = 'ssh'
	
		try:
			do_restore = Configure('Set',CONNECTION_TYPE, USER_NAME, PASSWORD, SERVER_IP, DEVICES_IP, EN_PASS, CONF_NAME)
			return redirect('devices')

		except Exception as e:
			raise e


def reset_pass(request):
	pass


def restore_os():
	pass


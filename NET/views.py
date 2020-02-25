from django.shortcuts import render
from .utils.utils import Configure, SnmpSet
from subprocess import run,PIPE
from django.http import HttpResponse


def login(request):
	return render(
		request, 
		'login.html',
		)


def index(request):
	return render(
		request,
		'index.html',
		)

def snmp(request):
	return render(
		request, 
		'snmptraps_setting.html',
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
		return render(
			request, 
			'snmptraps_setting.html',
			)

	except Exception as e:
		raise e

def save_conf(request):
	print(request.POST)
	USER_NAME = request.POST.get('USER_NAME')
	PASSWORD = request.POST.get('PASSWORD') 
	SERVER_IP = request.POST.get('SERVER_IP')
	DEVICES_IP = request.POST.get('DEVICES_IP')
	EN_PASS = request.POST.get('EN_PASS')
	CONF_NAME = request.POST.get('CONF_NAME')
	if 'telnet_save' in request.POST:
		CONNECTION_TYPE = 'telnet'
		
		
		try:
			
			do_restore = Configure('Save',CONNECTION_TYPE, USER_NAME, PASSWORD, SERVER_IP, DEVICES_IP, EN_PASS, CONF_NAME)
			
			return render(
				request, 
				'devices.html',
				)

		except Exception as e:
			raise e
			return render(
				request, 
				'devices.html',
				)
	elif 'ssh_save' in request.POST:
		CONNECTION_TYPE = 'ssh'
	
		try:
			do_restore = Configure('Save',CONNECTION_TYPE, USER_NAME, PASSWORD, SERVER_IP,
				DEVICES_IP, EN_PASS, CONF_NAME)
			return render(
				request, 
				'devices.html',
				)

		except Exception as e:
			raise e
		
def set_conf(request):
	CONNECTION_TYPE = request.POST.get('connectMethod')
	USER_NAME = request.POST.get('username')
	PASSWORD = request.POST.get('PASSWORD') 
	SERVER_IP = request.POST.get('SERVER_IP')
	DEVICES_IP = request.POST.get('DEVICES_IP')
	CONF_NAME = request.POST.get('CONF_NAME')
	try:
		do_restore = Configure('Set',CONNECTION_TYPE, USER_NAME, PASSWORD, SERVER_IP,
								 DEVICES_IP, EN_PASS, CONF_NAME)
		return render(
			request, 
			'devices.html',
			)
	except Exception as e:
		raise e

def reset_pass(request):
	pass


def restore_os():
	pass

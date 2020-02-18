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

def reconf(request):
	CONNECTION_TYPE = request.POST.get('connectMethod')
	USER_NAME = request.POST.get('username')
	PASSWORD = request.POST.get('PASSWORD') 
	SERVER_IP = request.POST.get('SERVER_IP')
	DEVICES_IP = request.POST.get('DEVICES_IP')
	try:
		do_restore = Configure(CONNECTION_TYPE, USER_NAME, PASSWORD, SERVER_IP, DEVICES_IP)
	except Exception as e:
		raise e
	


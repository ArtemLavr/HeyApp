from django.shortcuts import render
from .utils.utils import BU
from subprocess import run,PIPE

def index(request):
	return render(
		request,
		'index.html',
		)


def devices(request):
	return render(
		request, 
		'devices.html',
		)

def reconf(request):
	connect_method = request.POST.get('connectMethod')
	username = request.POST.get('username')
	PASSWORD = request.POST.get('PASSWORD') 
	SERVER_IP= request.POST.get('SERVER_IP')
	DEVICES_IP = request.POST.get('DEVICES_IP')
	try:
		do_restore = BU.restore_config(username, PASSWORD, SERVER_IP, DEVICES_IP)
	except Exception as e:
		raise e
	


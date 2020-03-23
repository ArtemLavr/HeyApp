from django.db import models



class Devices():
	d_name = models.TextField(null=False)
	TYPES= (
		('None', 'Введите тип устройства'),
		('cr','Cisco Router'),
		('cs','Cisco Switch'),
		('l', 'Linux'),
		('w', 'Windows'),
		('p', 'Поток'),
		('u','Неизвестное устройство') 
		)
	d_type = models.CharField(max_length=1, choices='TYPES',null=False)
	d_id_address = models.TextField(null=False)
	d_last_update_time = models.DateTimeField(null=False)

class Events(models.Model):
	ev_text = models.TextField(null=False)
	user = models.TextField(null=False)
	ev_time = models.DateTimeField(null=False)
    
		
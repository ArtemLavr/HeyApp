from django.db import models

class Auth(models.Model):
	username = models.TextField(null = False)
	password = models.TextField(null = False)

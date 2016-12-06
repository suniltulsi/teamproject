from __future__ import unicode_literals
from django.db import models

<<<<<<< HEAD
<<<<<<< HEAD
class SignUp(models.Model):
	first_name=models.Charfield(max_length=120)
	last_name=models.Charfield(max_length=120)
	email=models.EmailField()
	password=models.Charfield(max_length=60)

	def __unicode__(self)
		return self.email


=======
# Create your models here.
class Signup(models.Model):
 	
 	userName = models.CharField(max_length = 15, unique = True)
 	email = models.EmailField(max_length = 40, unique = True)
 	password = models.CharField(max_length = 15, unique = True)

 	def __unicode__(self):
 		return self.email
 	
>>>>>>> master

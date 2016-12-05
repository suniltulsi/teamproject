from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Signup(models.Model):
 	first_Name = models.CharField(max_length = 25)
 	last_Name = models.CharField(max_length = 25)
 	DateOfBirth = models.DateField(auto_now = False, auto_now_add = False)
 	gender = models.BooleanField()
 	email = models.EmailField(max_length = 40, unique = True)
 	userName = models.CharField(max_length = 15, unique = True)
 	password = models.CharField(max_length = 15, unique = True)

 	def __unicode__(self):
 		return self.email
 	
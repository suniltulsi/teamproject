from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Signup(models.Model):
 	
 	userName = models.CharField(max_length = 15, unique = True)
 	email = models.EmailField(max_length = 40, unique = True)
 	password = models.CharField(max_length = 15, unique = True)

 	def __unicode__(self):
 		return self.email
 	
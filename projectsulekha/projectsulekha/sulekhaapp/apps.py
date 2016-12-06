from __future__ import unicode_literals

from django.apps import AppConfig
from .models import Signup 


class SulekhaappConfig(AppConfig):
    name = 'sulekhaapp'

class SignupAdmin(admin.ModelAdmin):
	list_display = ['id','fName','lName','email','userName','password']
	class Meta:
		model = Signup

admin.site.register(Signup,SignupAdmin)

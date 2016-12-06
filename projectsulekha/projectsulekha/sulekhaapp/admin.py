from django.contrib import admin
from .models import SignUp

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email','password']
	class Meta:
		model = SignUp

admin.site.register(SignUp,SignUpAdmin)
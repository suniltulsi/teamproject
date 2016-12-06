from django.contrib import admin
<<<<<<< HEAD
from .models import SignUp

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email','password']
	class Meta:
		model = SignUp

admin.site.register(SignUp,SignUpAdmin)
=======
from .models import Signup

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
	list_display = ['userName','email','password']
	class Meta:
		model = Signup

admin.site.register(Signup,SignupAdmin)
>>>>>>> master

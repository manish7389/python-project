from atexit import register
from django.contrib import admin
from register.models  import register
# Register your models here.

class registerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','password')

admin.site.register(register,registerAdmin)

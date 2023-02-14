from django.contrib import admin
from services.models import services

class servicesAdmin(admin.ModelAdmin):
    list_display=("services_icon","services_title","services_des")

admin.site.register(services,servicesAdmin)
# Register your models here.


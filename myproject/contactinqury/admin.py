from django.contrib import admin
from contactinqury.models import contactinqury

class contactinquryAdmin(admin.ModelAdmin):
    list_display = ("name","last_name","email","phone","massage")

admin.site.register(contactinqury,contactinquryAdmin)
# Register your models here.

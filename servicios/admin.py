from django.contrib import admin
from .models import Servicio

# Register your models here.
#admin.site.register(Servicio)

class AdminServicio(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio,AdminServicio)
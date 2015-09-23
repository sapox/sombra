from django.contrib import admin

# Register your models here.
from .models import Sombra

class SombraAdmin(admin.ModelAdmin):
	list_display = ('cadaver')

admin.site.register(Sombra)
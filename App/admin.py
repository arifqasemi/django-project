from django.contrib import admin
from .models import User
# Register your models here.
class AdminDisplay(admin.ModelAdmin):
    list_display = ('email', 'password','image')
admin.site.register(User, AdminDisplay)

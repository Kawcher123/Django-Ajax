from django.contrib import admin
from .models import USer
# Register your models here.

@admin.register(USer)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
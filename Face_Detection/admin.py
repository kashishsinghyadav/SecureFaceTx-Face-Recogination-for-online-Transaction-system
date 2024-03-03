from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('face_id','name','address','phone','email','image')


admin.site.register(UserProfile,UserAdmin)
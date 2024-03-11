from django.contrib import admin
from .models import OTP

class OtpAdmin(admin.ModelAdmin):
    list_display = ('email', 'otp', 'created_at')

admin.site.register(OTP, OtpAdmin)

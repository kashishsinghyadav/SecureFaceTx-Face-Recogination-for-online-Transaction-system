from django.contrib import admin
from .models import *
class BankAdmin(admin.ModelAdmin):
    list_display=('account_holder','routing_number','account_type')

admin.site.register(Bankmodel,BankAdmin)


class CreditAdmin(admin.ModelAdmin):
    list_display=('name_on_card','card_number','expiry_mm','cvv')

admin.site.register(Creditmodel,CreditAdmin)
# Register your models here.

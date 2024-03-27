from django.contrib import admin
from django.urls import path
from payments.views import make_payment,payment_success

urlpatterns = [
       path('make-payment/', make_payment, name='make_payment'),
    path('payment-success/', payment_success, name='payment_success'),


]

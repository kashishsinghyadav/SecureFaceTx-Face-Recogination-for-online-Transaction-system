from django.shortcuts import render

# Create your views here.
import razorpay
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Payment
 
def make_payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        if name and amount:
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            order_amount = int(float(amount) * 100)
            order_currency = 'INR'
            order_receipt = 'order_rcptid_11'

            order = client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt, payment_capture='0'))

            payment = Payment.objects.create(name=name, amount=amount, razorpay_order_id=order['id'])
            payment.save()
            return render(request, 'faceDetection/payment_checkout.html', {'order': order})
    return render(request, 'faceDetection/make_payment.html')


def payment_success(request):
    # Handle payment success here
    return render(request, 'faceDetection/payment_success.html')

from django.shortcuts import render
from django.http import HttpResponse # for returning the response
from django.urls import reverse
from django_daraja.mpesa.core import MpesaClient

# Create your views here.


def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
 
    phone_number = '0741151005'
    amount = 1
    account_reference = 'account number'
    transaction_desc = 'stk push test'
   # callback_url=request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
   # print(response)
    return HttpResponse(response)
    

def stk_push_callback(request):       
    stk_data = index
    return HttpResponse(stk_data)

# def BusinessPayment(request):
#     cl = MpesaClient()
#     phone_number = '0741151005'
#     amount = 2
#     transaction_desc = 'Business Payment '
#     occassion = 'suppliers'
#  #   callback_url = request.build_absolute_uri(reverse('mpesa_business_payment_callback'))
#     callback_url='https://darajambili.herokuapp.com/b2c/result'
#     response = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
#     return HttpResponse(response)
    
# def SalaryPayment(request):
#     cl = MpesaClient()
#     phone_number = '0741151005'
#     amount = 3
#     transaction_desc = 'Salary Payment '
#     occassion = 'Employees'
#   #  callback_url = request.build_absolute_uri(reverse('mpesa_business_payment_callback'))
#     callback_url='https://darajambili.herokuapp.com/b2c/result'
#     response = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
#     return HttpResponse(response)

# def PromotionPayment(request):
#     cl = MpesaClient()
#     phone_number = '0741151005'
#     amount = 4
#     transaction_desc = 'Promotion Payment '
#     occassion = 'Promotion'
#     #callback_url = request.build_absolute_uri(reverse('mpesa_business_payment_callback'))
#     callback_url='https://darajambili.herokuapp.com/b2c/result'
#     response = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
#     return HttpResponse(response)
    



       


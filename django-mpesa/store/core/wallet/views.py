
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0710568014'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

    if response.status_code == 200:
        # return HttpResponse(response)
        # redirect to a call back page
        # save the response to a database
        print(response)
        return redirect('stk_push_callback')
    else:
        return HttpResponse("Error")
    # return HttpResponse(response)

# def index(request):
#     return render(
#         request,
#         'index.html',
#         {
#             'title': 'SSA Payments',
#             'message': 'Payments made easy!',
#             'year': datetime.now().year,
#         }
#     )


def daraja_stk_push_callback(request):
    data = request.body
        
    return HttpResponse("STK Push in Django")
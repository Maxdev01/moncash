from django.shortcuts import render
import moncashify



# Create your views here.
def home(request):
    if request.method == 'POST':
        secret_key = 'MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhANMaWxcDGmrUl5DsVGoYhYHW3o4YYUShnNvHrugor9BVAgMBAAE='
        client_id = '088a6f9bfc2d84a59a1f964119adf67e'
        order_id = 'JHDLK77'
        amount = 1000

        moncash = moncashify.API(client_id, secret_key, True)
        try:
            payment = moncash.payment(order_id, amount)
        except Exception as e:
            print('error', e)
        print(payment.redirect_url)


        # print('details', payment.get_response())
    else:
        pass
    return render(request, 'home.html', {})

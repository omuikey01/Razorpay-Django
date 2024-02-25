from django.shortcuts import render
import razorpay
from .models import Payment

# Create your views here.

def homepage(request):
    if request.method == 'POST':
        name = request.POST['pname']
        amt = int(request.POST['pamt']) * 100
        client = razorpay.Client(auth=("rzp_test_e8NTJnBYWuTCtM", "QtzHhrBJPXx9IWtrpUK6TZJP"))
        data = { "amount": amt, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        print(payment)
        return render(request, "index.html", { "status" : payment })
    
    return render(request, "index.html")













 # if payment.status == 'created' :
        #     Payment.objects.create(order_id = payment.id,
        #                        product_name = name,
        #                        product_amount = amt,
        #                        created_at = payment.created_at)
        # else :
        #     return render(request, "index.html", { "msg" : "Some Server Issue" })
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from customers.models import Customer
from products.models import ProductComment

# Create your views here.

def index(request):
    customers = Customer.objects.all().filter(is_published=True)[0:3]
    comments = ProductComment.objects.all().filter(is_published=True, rating__gte=3).order_by('-list_date')[0:3]

    context = {
        'customers': customers,
        'comments': comments
    }
    return render(request, 'pages/index.html', context)


def about(request):
    comments = ProductComment.objects.all().filter(is_published=True, rating__gte=3).order_by('-list_date')[0:6]

    context = {
        'comments': comments
    }
    return render(request, 'pages/about.html', context)

def emailcontact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']

        # Send email
        send_mail(
            'Your Query on Jindal Trading Company',
            'Your Name : "' + name + '".\nYour Email : "' + email + '"\n\nYour Query : "' + query + '".\n\nWe will contact you very soon.\n\n',
            'abcdef7700000000@gmail.com',
            ['manishbainsla1072@gmail.com', email],
            fail_silently=False
        )
        messages.success(request, 'We have recieved your Query. We will contact you soon.')
        return redirect('index')

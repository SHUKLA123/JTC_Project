from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact,ServiceContact

# Create your views here.

def contact(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        product = request.POST['product']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        order = request.POST.get('order', False)
        address = request.POST['address']

        if order == 'on':
            order = True
        else:
            order = False

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(product_id=product_id, user_id=user_id)

            if has_contacted:
                messages.error(request, "You have already made an inquiry for this product, Try Contacting through official EMAIL or PHONE NO. of Company.")
                return redirect('/products/'+product_id)

        contact = Contact(product=product, product_id=product_id, name=name, email=email, phone=phone, address=address, message=message, user_id=user_id, order=order)
        contact.save()

        # Send email
        send_mail(
            'Product Inquiry',
            'There has been an Inquiry for ' + product + '. Sign into Admin Panel for more Information.' + address,
            'abcdef7700000000@gmail.com',
            ['manishbainsla1072@gmail.com'],
            fail_silently=False
        )

        messages.success(request, "Your request has been submitted, someone will contact you soon.")
    return redirect('/products/'+product_id)


def service_contact(request):
    if request.method == "POST":
        service_id = request.POST['service_id']
        service = request.POST['service']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        address = request.POST['address']
        print(address)
        order = request.POST.get('order', False)

        if order == 'on':
            order = True
        else:
            order = False

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = ServiceContact.objects.all().filter(service_id=service_id, user_id=user_id)

            if has_contacted:
                messages.error(request, "You have already made an inquiry for this product, Try Contacting through official EMAIL or PHONE NO. of Company.")
                return redirect('/products/service/'+service_id)

        contact = ServiceContact(service=service, service_id=service_id, name=name, email=email, phone=phone, address=address, message=message, user_id=user_id, order=order)
        contact.save()

        # Send email
        send_mail(
            'Product Inquiry',
            'There has been an Inquiry for ' + service + '. Sign into Admin Panel for more Information.',
            'abcdef7700000000@gmail.com',
            ['manishbainsla1072@gmail.com'],
            fail_silently=False
        )

        messages.success(request, "Your request has been submitted, someone will contact you soon.")
    return redirect('/products/service/'+service_id)

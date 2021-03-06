from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from contacts.models import Contact, ServiceContact

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken.')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already registered.')
                    return redirect('register')

                else:
                    # Details are correct
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    # Login after registeration automatically
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in.')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can login.')
                    return redirect('login')


        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        messages.success(request, 'Testing success message.')
        # Register User
        return redirect('register')

    else:
        return render(request, 'accounts/register.html', {})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # Login User
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')

        else:
            messages.error(request, 'Username or Password is incorrect.')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html', {})

@login_required
def logout(request):
    # if request.method == "POST":
    auth.logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('index')

#niranjan
@login_required
def dashboard(request):
    user_contacts = Contact.objects.all().filter(user_id=request.user.id).order_by('-contact_date')
    service_contacts = ServiceContact.objects.all().filter(user_id=request.user.id).order_by('-contact_date')
    context = {
        'user_contacts': user_contacts,
        "service_contacts" : service_contacts,
    }
    return render(request, 'accounts/dashboard.html', context)

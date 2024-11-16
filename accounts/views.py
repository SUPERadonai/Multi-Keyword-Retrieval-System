from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact_new
from realtors.models import Realtor
from contacts.models import Fav
from listings.models import Listing, Listing_new, Listing_old


# from listings.models import Listing


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        usertype = request.POST['user']

        # Check if passwords match
        if password == password2:
            #  Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                        first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can Log In')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usertype = request.POST['user']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard_house')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')


def dashboard_house(request):

    # context = {
    #     'house': ,
    # }

    return render(request, 'accounts/dash_house.html')

def dashboard_fav(request):

    context = {
        'fav': 1,
    }

    return render(request, 'accounts/dash_fav.html', context)


def fav_delete(request):
    if request.method == "POST":
        defav_id = request.POST['fav_id']


    return redirect('dashboard_fav')

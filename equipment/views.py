from django.shortcuts import render
from .models import Equipment, Rental, MaintenanceLog


def homepage(request):
    return render(request, 'homepage.html')


def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipments': equipments})

def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'rental_list.html', {'rentals': rentals})

def maintenance_list(request):
    logs = MaintenanceLog.objects.all()
    return render(request, 'maintenance_list.html', {'logs': logs})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request,'index.html')

# equipment/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']

        # Check if the username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        # Create the user if username and email are unique
        user = User.objects.create_user(username=uname, email=email, password=password,
                                        first_name=fname, last_name=lname)
        login(request, user)  # Log the user in after registration
        return redirect('homepage')  # Redirect to home page after successful registration

    return render(request, 'register.html')



def login_user(request):
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')


# views.py
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # Logout the user
    return redirect('homepage')  # Redirect to home after logout

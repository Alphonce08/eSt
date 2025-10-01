from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Register
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, auth


# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        
        email = request.POST.get['email']
        password = request.POST.get['password']
        confirmpassword = request.POST.get['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                User = User.objects.create(username=username, email=email, password=password)
                user.save()
                print('user created')
                return redirect('login')
                
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
     return render(request, 'register.html')


# def register(request):
#     if request.method == 'POST':
#         form = Register(request.POST)
#         if form.is_valid():
#             # Process the form data (e.g., save to database)
#             return redirect('index')  # Redirect to a success page
#     else:
#         form = Register()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Generate a random OTP
#         otp = random.randint(100000, 999999)

#         # Send OTP to the user's email
#         subject = 'Your OTP Code'
#         message = f'Hello {username},\n\nYour OTP code is: {otp}\n\nThank you!'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email]

#         try:
#             send_mail(subject, message, email_from, recipient_list)
#             messages.success(request, f'OTP has been sent to {email}.')
#         except Exception as e:
#             messages.error(request, f'Error sending email: {e}')

#          # Here you can save the user data and OTP to the database if needed

#          # Redirect to a page where the user can enter the OTP (not implemented here)
           
#     return render(request, 'register.html', {'form': form})
def login(request):
    if request.POST.get == "POST":
        username.request.get == ['username']
        password.request.get == ['password']
        user = Register.objects.filter(username=username, password=password).first()
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            messages.info(request, 'Invalid username or password')
        return redirect('login')  # Redirect to a success page
    else:
     return render(request, 'index.html')

     def logout(request):
         auth.logout(request)
         return redirect('index')






        
    

        

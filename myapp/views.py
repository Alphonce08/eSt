from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.core.mail import send_mail
from .models import EmailOTP
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def footer(request):
    return render(request, 'footer.html')


def register(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.is_active = False  # Deactivate account untill verified
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()

            otp_entry = EmailOTP.objects.create(user=user)
            otp = otp_entry.generate_otp()
            # Send OTP to user's email

            send_mail(
                'Your Email Verification Code',
                f'Your OTP code is {otp}',
                'wisoft33@gmail.com', # From email
                [user.email],
                fail_silently=False,
            )

            messages.info(request, "We sent an OTP to your email. Please verify.")
            return redirect('verify_otp')
    else:
        form = User()
    return render(request, 'register.html', {'form': form})






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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')  # Redirect to a success page.
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to login page.
    return render(request, 'login.html')

        
    

        

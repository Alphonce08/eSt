
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import EmailOTP
from .forms import RegisterForm  # ✅ import the form

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

def payment(request):
    return render(request, 'payment.html')

def forgot_password(request):
    return render(request, 'login/forgot_password.html')




def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username=email, email=email, password=password, is_active=False)
        
        otp_rec = EmailOTP.objects.create(user=user)
        otp = otp_rec.generate_otp()

        send_mail(
            subject="Your OTP Code",
            message=f"Your OTP is {otp}. It expires in 5 minutes.",
            from_email='tkip1953@gmail.com',
            recipient_list=[email],
        )
        return redirect("verify_otp")
    return render(request, "register.html")


def verify_otp(request):
    if request.method == "POST":
        email = request.POST['email']
        code = request.POST['otp']

        user = User.objects.get(email=email)
        otp_entry = EmailOTP.objects.get(user=user)

        if not otp_entry.is_expired() and otp_entry.otp == code:
            user.is_active = True
            user.save()
            return redirect("login")
        else:
            return render(request, "verify.html", {"error": "Invalid or expired OTP"})

    return render(request, "verify_otp.html")


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

        
    

        

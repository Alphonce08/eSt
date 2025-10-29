import random, string, datetime
from django.db import models
from django.contrib.auth.models import User

class EmailOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        code = ''.join(random.choices(string.digits, k=6))
        self.otp = code
        self.created_at = datetime.datetime.now()
        self.save()
        return code

    def is_expired(self):
        return (datetime.datetime.now(datetime.timezone.utc) - self.created_at).seconds > 300 # 5 minutes


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

    return render(request, "verify.html")

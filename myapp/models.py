from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone
from datetime import timedelta


class EmailOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def generate_otp(self):
        # Generate and store a 6 digit OTP

        otp = ''.join(random.choice(string.digits, k=6))
        self.otp = otp
        self.expires_at = timezone.now() + timedelta(minutes=5)
        self.save()
        return otp
        

    def is_expired(self):
        return timezone.now(self.expires_at)    

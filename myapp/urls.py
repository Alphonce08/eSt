from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('base/', views.base, name='base'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('footer/', views.footer, name='footer'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),  
    path('payment/', views.payment, name='payment'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]
   


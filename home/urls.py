from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about-us/', views.aboutUs, name='about'),
    path('laws/', views.laws, name='laws'),
    path('contact-us/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('privacy-policy/', views.privacy, name='privacy'),
]
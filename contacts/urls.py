from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('servicecontact/', views.service_contact, name = "servicecontact")
]

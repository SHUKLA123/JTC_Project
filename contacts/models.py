from django.db import models

from datetime import datetime

# Create your models here.

class Contact(models.Model):
    product = models.CharField(max_length=300)
    product_id = models.IntegerField()
    name = models.CharField(max_length=180)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, max_length=1000)
    message = models.TextField(blank=True, max_length=1000)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    order = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.contact_date}"


#Niranjan

class ServiceContact(models.Model):
    service = models.CharField(max_length=200)
    service_id = models.IntegerField()
    name = models.CharField(max_length=180)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, max_length=1000)
    message = models.TextField(blank=True, max_length=1000)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    order = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.contact_date}"

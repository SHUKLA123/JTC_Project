from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    local_name = models.CharField(blank=True, max_length=200)

    category = models.CharField(max_length=200)
    price = models.FloatField()
    size = models.CharField(max_length=150, blank=True)
    pattern = models.CharField(max_length=150, blank=True)
    thickness = models.CharField(max_length=150, blank=True)

    brand_name = models.CharField(max_length=250, blank=True)

    customisable = models.BooleanField(default=False)

    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    detail_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    detail_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    detail_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    description = models.TextField(max_length=1500, blank=True)

    amazon_link = models.CharField(blank=True, null=True, max_length=1000)
    flipkart_link = models.CharField(blank=True, null=True, max_length=1000)

    is_published = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)

    list_date = models.DateTimeField(default=datetime.now, blank=True)


    # str method
    def __str__(self):
        return f"{self.name} - {self.category}"


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    detail_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    detail_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    detail_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField(null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.list_date}"





class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comment")
    name = models.CharField(max_length=150)
    comment = models.TextField(max_length=350)
    rating = models.PositiveIntegerField(default=5) # check in view if rating in greater then 5
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return f"{self.name} {self.rating}"

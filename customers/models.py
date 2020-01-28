from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', default='img/dummy.png')
    location = models.CharField(max_length=500)
    task = models.CharField(max_length=300)
    description = models.TextField(blank=False, max_length=1500)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} from {self.location}"

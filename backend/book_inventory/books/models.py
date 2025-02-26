from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    published_date=models.DateField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    
    def __str__(self):
        return self.title


    

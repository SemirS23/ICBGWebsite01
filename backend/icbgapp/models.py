from django.db import models

# Create your models here.

class Event(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()  
    image=models.ImageField()
    slug=models.SlugField(max_length=255)
    date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=10)


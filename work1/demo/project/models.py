from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
sub = (
    ('yearly', 'YEARLY'),
    ('monthly', 'MONTHLY'),
)


class Post(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    cover = models.ImageField(upload_to='images/')
    sub = models.CharField(max_length=10, choices=sub, default='MONTHLY')
    date = models.DateField()

    def __str__(self):
        return self.name


class Category(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    des = models.TextField()


    def __str__(self):
        return self.name


class Audio(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    des = models.TextField()
    audio = models.FileField(upload_to='audio/')
    cg = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub = models.CharField(max_length=10, choices=sub, default='MONTHLY')
    date = models.DateField()
    def __str__(self):
        return self.name


class Pic(models.Model):
    img = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
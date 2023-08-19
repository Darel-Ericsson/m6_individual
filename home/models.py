from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, null=False, unique=True)
    rut = models.CharField(max_length=50,  null=True)
    email = models.EmailField(max_length=254,  null=False,  unique=True, )
    phone = models.CharField(max_length=15, null=True)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    password = models.CharField(max_length=128, null=True)

    # def save(self, *args, **kwargs):
    #     self.username = self.email
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.username
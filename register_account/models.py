from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    ROLE_CHOICES =(
        ('customer','Customer'),
        ('admin', 'Admin')
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length= 10)
    role =  models.CharField(max_length=20, default='customer', choices= ROLE_CHOICES)

    def __str__(self):
        return self.username     

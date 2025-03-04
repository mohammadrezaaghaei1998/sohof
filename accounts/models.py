from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


# class CustomUser(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('buyer', 'Buyer'),
#         ('seller', 'Seller'),
#     )
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='buyer')

#     email = models.EmailField(unique=True)
    
#     USERNAME_FIELD = 'email' 
#     REQUIRED_FIELDS = ['username']  

#     def __str__(self):
#         return f"{self.email} ({self.user_type})"




class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='buyer')

    email = models.EmailField(unique=True)

    # Add username back for sellers
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.user_type})"

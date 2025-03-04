from django.db import models
from accounts.models import CustomUser
from django.contrib.auth.models import User
from companies.models import Product
from django.conf import settings


# Create your models here.



class BuyerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="buyer_profile")
    name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    tax_number = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='buyer_profile_images/', blank=True, null=True)
    
    def __str__(self):
        return f"Buyer Profile: {self.user.username}"
    



class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
# core/models.py

from django.db import models
from django.contrib.auth.models import User

# This model represents a product in our e-commerce store
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# This model tracks user behavior
class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # The interaction_type could be 'view', 'purchase', or 'rating'
    interaction_type = models.CharField(max_length=50)
    rating = models.IntegerField(null=True, blank=True) # For product ratings
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.interaction_type} - {self.product.name}'
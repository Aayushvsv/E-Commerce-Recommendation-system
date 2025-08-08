# core/serializers.py

from rest_framework import serializers
from .models import Product, UserInteraction

# Serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Serializer for the UserInteraction model
class UserInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInteraction
        fields = '__all__'
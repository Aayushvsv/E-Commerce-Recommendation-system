# core/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import ProductSerializer, UserInteractionSerializer
from .models import Product, UserInteraction

from django.contrib.auth.models import User
import os
import torch
import numpy as np

# Import the RecommenderNet model and the training script's helper functions
from core.recommender.model import RecommenderNet
from core.management.commands.train_model import Command as TrainCommand

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def recommend(self, request):
        # This is a placeholder user ID for now
        # You would get this from the logged-in user in a real application
        user_id = 0  # Assuming user ID 0 exists for our fake data

        # Get the total number of users and items for the model
        num_users = 100
        num_items = Product.objects.count()

        # Load the trained model
        model = RecommenderNet(num_users, num_items)
        model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recommender', 'recommender_model.pt')

        try:
            model.load_state_dict(torch.load(model_path))
            model.eval()
        except FileNotFoundError:
            return Response({"error": "Model not found. Please train the model first."}, status=status.HTTP_404_NOT_FOUND)

        # Get the list of all products from the database
        all_products = list(Product.objects.all())

        # Generate a list of all product indices
        product_indices = np.arange(num_items)

        # Map products from the database to their integer indices
        product_id_map, _ = TrainCommand().get_product_map()

        # Create tensors for prediction
        user_tensor = torch.LongTensor([user_id] * num_items)
        item_tensor = torch.LongTensor(product_indices)

        # Get predictions for all products for the given user
        with torch.no_grad():
            predictions = model(user_tensor, item_tensor).numpy().flatten()

        # Get the top 5 product indices with the highest predicted ratings
        top_5_indices = predictions.argsort()[-5:][::-1]

        # Get the corresponding product objects
        recommended_products = [all_products[i] for i in top_5_indices]

        # Serialize and return the products
        serializer = ProductSerializer(recommended_products, many=True)
        return Response(serializer.data)

class UserInteractionViewSet(viewsets.ModelViewSet):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer
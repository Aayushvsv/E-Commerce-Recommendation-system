# backend/core/management/commands/train_model.py

from django.core.management.base import BaseCommand
from core.models import Product
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
import numpy as np
import os

from core.recommender.model import RecommenderNet
from core.recommender.data import generate_fake_data

# --- Training Configuration ---
NUM_EPOCHS = 10
EMBEDDING_DIM = 50
LEARNING_RATE = 0.01

class Command(BaseCommand):
    help = 'Trains the recommender model using PyTorch.'

    def get_product_map(self):
        products = list(Product.objects.all().values_list('id', flat=True))
        product_id_map = {str(product_uuid): i for i, product_uuid in enumerate(products)}
        return product_id_map, len(products)

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting model training...")

        # Load data
        fake_data = generate_fake_data(num_items=Product.objects.count())
        product_map, num_items = self.get_product_map()
        num_users = fake_data['user_ids'].max() + 1

        # Get the list of all products
        all_products = list(Product.objects.all())
        # Map product UUIDs to integers based on the order
        mapped_item_ids = np.array([product_map[str(all_products[i].id)] for i in fake_data['item_ids']])

        # Convert data to PyTorch tensors
        user_tensor = torch.LongTensor(fake_data['user_ids'])
        item_tensor = torch.LongTensor(mapped_item_ids)
        rating_tensor = torch.FloatTensor(fake_data['ratings'])

        # Create a TensorDataset and DataLoader
        dataset = TensorDataset(user_tensor, item_tensor, rating_tensor)
        dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

        # Initialize model
        model = RecommenderNet(num_users, num_items, embedding_dim=EMBEDDING_DIM)
        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

        # Training loop
        for epoch in range(NUM_EPOCHS):
            for user_ids, item_ids, ratings in dataloader:
                optimizer.zero_grad()
                outputs = model(user_ids, item_ids)
                loss = criterion(outputs, ratings)
                loss.backward()
                optimizer.step()
            self.stdout.write(f"Epoch {epoch+1}/{NUM_EPOCHS}, Loss: {loss.item():.4f}")

        # Save the trained model
        model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'recommender', 'recommender_model.pt')
        torch.save(model.state_dict(), model_path)
        self.stdout.write(self.style.SUCCESS(f"\nModel trained and saved to {model_path}"))
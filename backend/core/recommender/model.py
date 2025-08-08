# core/recommender/model.py

import torch
import torch.nn as nn

class RecommenderNet(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim=50):
        super().__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
        
        self.fc_layers = nn.Sequential(
            nn.Linear(embedding_dim * 2, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, user_ids, item_ids):
        user_embedded = self.user_embedding(user_ids)
        item_embedded = self.item_embedding(item_ids)

        combined_embeddings = torch.cat([user_embedded, item_embedded], dim=1)
        
        output = self.fc_layers(combined_embeddings)
        return output.squeeze()
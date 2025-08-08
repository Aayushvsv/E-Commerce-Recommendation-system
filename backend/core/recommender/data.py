# backend/core/recommender/data.py

import numpy as np

def generate_fake_data(num_users=100, num_items=10):
    # Generate random user and item IDs
    user_ids = np.random.randint(0, num_users, size=500)
    item_ids = np.random.randint(0, num_items, size=500)

    # Generate random ratings (e.g., 1-5 stars)
    ratings = np.random.randint(1, 6, size=500)

    # Create a dictionary to hold our data
    data = {
        'user_ids': user_ids,
        'item_ids': item_ids,
        'ratings': ratings
    }
    return data

if __name__ == '__main__':
    fake_data = generate_fake_data()
    print("Generated fake data with user IDs, item IDs, and ratings.")
    print("User IDs:", fake_data['user_ids'][:5])
    print("Item IDs:", fake_data['item_ids'][:5])
    print("Ratings:", fake_data['ratings'][:5])
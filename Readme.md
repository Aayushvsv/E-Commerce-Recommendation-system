# E-commerce Recommendation System

A full-stack e-commerce platform with intelligent product recommendations powered by machine learning.

## 🎯 Overview

This project demonstrates the integration of modern web development with machine learning by building an e-commerce platform that learns from user behavior to provide personalized product recommendations. The system uses collaborative filtering with PyTorch to analyze user interactions and suggest relevant products.

## ✨ Features

- **🔐 User Authentication** - Secure registration and login system
- **🛍️ Product Catalog** - Dynamic product management through Django Admin
- **📊 Behavior Tracking** - Monitors user interactions (views, purchases, ratings)
- **🧠 AI Recommendations** - Neural network-powered personalized suggestions
- **🔌 RESTful API** - Clean API endpoints for seamless data exchange
- **📱 Responsive Frontend** - Modern, mobile-friendly user interface

## 🛠️ Technology Stack

| Layer | Technologies |
|-------|--------------|
| **Backend** | Python, Django, Django REST Framework |
| **Database** | SQLite |
| **Machine Learning** | PyTorch, NumPy |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) |
| **Development** | Git, pip, VS Code |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git
- VS Code with Live Server extension (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aayushvsv/E-Commerce-Recommendation-system.git
   cd E-Commerce-Recommendation-system
   ```

2. **Set up the backend**
   ```bash
   cd backend
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Initialize database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Train the ML model**
   ```bash
   python manage.py train_model
   ```
   > This creates `recommender_model.pt` in `backend/core/recommender/`

5. **Start the backend server**
   ```bash
   python manage.py runserver
   ```

6. **Launch the frontend**
   - Open `frontend/index.html` with VS Code Live Server
   - Access via `http://127.0.0.1:5500` (or your Live Server port)

## 📖 Usage

### Admin Dashboard
- Navigate to `http://127.0.0.1:8000/admin/`
- Login with your superuser credentials
- Add and manage products, view user interactions

### Customer Interface
- Browse products on the main page
- View personalized recommendations
- Interact with products to improve future suggestions

## 📁 Project Structure

```
E-Commerce-Recommendation-system/
├── backend/
│   ├── core/
│   │   ├── recommender/     # ML model and training logic
│   │   ├── models.py        # Database models
│   │   └── views.py         # API endpoints
│   ├── requirements.txt     # Python dependencies
│   └── manage.py           # Django management script
└── frontend/
    ├── index.html          # Main page
    ├── styles.css          # Styling
    └── script.js           # Frontend logic
```

## 🔧 API Endpoints

- `GET /api/products/` - Retrieve all products
- `GET /api/recommendations/<user_id>/` - Get user recommendations
- `POST /api/interactions/` - Record user interactions
- `POST /api/auth/login/` - User authentication

## 🤖 Machine Learning Model

The recommendation system uses a collaborative filtering approach with:
- **Neural Collaborative Filtering (NCF)** architecture
- User and item embeddings
- Multiple hidden layers with dropout
- Training on user-item interaction data

## 🧪 Development

### Adding New Features

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

### Running Tests

```bash
cd backend
python manage.py test
```

## 📊 Model Performance

The recommendation model is trained on user interaction data and evaluated using metrics like:
- Mean Squared Error (MSE)
- Precision@K
- Recall@K

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues and pull requests. For major changes, please open an issue first to discuss your proposed changes.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built as a learning project to demonstrate ML integration in web applications
- Inspired by modern e-commerce recommendation systems
- Thanks to the Django and PyTorch communities for excellent documentation

---

⭐ **Star this repository if it helped you learn something new!**

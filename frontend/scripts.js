// frontend/script.js

const productsContainer = document.getElementById('products-container');
const recommendationsContainer = document.getElementById('recommendations-container');

// ... (Your fetchProducts function is here) ...

async function fetchRecommendations() {
    try {
        // Fetch data from your new recommendations API endpoint
        const response = await fetch('http://127.0.0.1:8000/api/products/recommend/');

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const recommendations = await response.json();
        console.log('Fetched recommendations:', recommendations);

        // Clear existing content
        recommendationsContainer.innerHTML = '';

        // Loop through the recommendations and display them
        recommendations.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';

            productCard.innerHTML = `
                <img src="${product.image_url}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p class="price">$${product.price}</p>
            `;
            recommendationsContainer.appendChild(productCard);
        });

    } catch (error) {
        console.error('Could not fetch recommendations:', error);
        recommendationsContainer.innerHTML = '<p>Failed to load recommendations.</p>';
    }
}

// Call both functions when the page loads
document.addEventListener('DOMContentLoaded', () => {
    fetchProducts();
    fetchRecommendations(); // Add this line
});
const productSelect = document.getElementById('product');
const productList = document.getElementById('product-list');
const requestList = document.getElementById('request-list');
const form = document.getElementById('request-form');
const message = document.getElementById('message');

        // Permet d'afficher tout les produits
        fetch('/api/products/')
            .then(res => res.json())
            .then(data => {
                data.forEach(product => {
                    // La liste
                    const li = document.createElement('li');
                    li.textContent = `${product.name} - ${product.quantity} en stock - ${product.price} €`;
                    productList.appendChild(li);

                    // Select
                    const option = document.createElement('option');
                    option.value = product.id;
                    option.textContent = product.name;
                    productSelect.appendChild(option);
                })
            })
        
        // Remplit la liste  des produits
        fetch('/api/products/')
            .then(response => response.json())
            .then(data => {
                const select = document.getElementById('product');
                data.forEach(product => {
                    const option = document.createElement('option');
                    option.value = product.id;
                    option.textContent = `${product.name} (${product.quantity} en stock)`;
                    select.appendChild(option);
                });
            });

        // Soumettre une demande
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const productId = productSelect.value;
            const quantity = document.getElementById('quantity').value;

            fetch('/api/requests/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),  // ou getCSRFToken() selon ta fonction
                },
                body: JSON.stringify({
                    product: productId,
                    quantity_requested: quantity,
                })
            })
            .then(res => {
                if (res.ok) {
                    message.textContent = "Demande envoyée avec succès";
                    fetchUserRequests();
                    form.reset();
                } else {
                    message.textContent = "Erreur lors de l'envoi";
                }
            });
        });

        // Affiche les demandes
        function fetchUserRequests() {
            fetch('/api/requests/')
                .then(response => response.json())
                .then(data => {
                    const list = document.getElementById('user-requests-list');
                    list.innerHTML = '';
                    data.forEach(request => {
                        const item = document.createElement('li');
                        item.textContent = `Produit ID ${request.product} — Quantité: ${request.quantity_requested} — Statut: ${request.status}`;
                        list.appendChild(item);
                    });
                });
        }

        fetchUserRequests();

        // Fonction CSRF
        function getCSRFToken() {
            let cookieValue = null;
            const name = 'csrftoken';
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

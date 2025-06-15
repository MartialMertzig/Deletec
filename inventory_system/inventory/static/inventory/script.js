const productSelect = document.getElementById('product-select');
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
                    const li = doucment.createElment('li');
                    li.textContent = '${product.name} - ${product.quantity} en stock - ${product.price} €';
                    productList.appendChild(li);

                    // Select
                    const option = docuement.createElement('option');
                    option.value = product.id;
                    option.textContent = product.name;
                    productSelect.appendChild(option);
                })
            })
        
        // Soumettre une demande
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const productId = productSelect.value;
            const quantity = document.getElementById('quantity').value;
            fetch('/api/requests/', {
                method: 'POST',
                headers: {
                    'Content-Type' : 'application/json',
                    'X-CSRFToken' : getCSRFToken(),
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
                    form.rest();
                }
                else {
                    message.textContent = "Erreur lor de l'envoi";
                }
            });
        });

        // Affiche les demandes
        function fetchUserRequests() {
            fetch('/api/requests/')
                .then(res => res.json())
                .then(data => {
                    requestList.innerHTML ='';
                    data.forEach(req => {
                        const li = document. createElement('li');
                        li.textContent = '${req.product} - ${req.quantity_requested} demandés - statut : ${req.status}';
                        requestList.appendChild(li);
                    });
                });
        }

        fetchUserRequests();

        // Fonction CSRF
        function getCSRFToken() {
            let cookieValue = null;
            const name = 'csrftoken';
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookies.split(';');
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
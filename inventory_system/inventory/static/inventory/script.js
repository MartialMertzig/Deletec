const form = document.getElementById('request-form'); // Formuler une demande
const message = document.getElementById('message'); // Message de réponse
const requestLinesContainer = document.getElementById('request-lines');
const addLineBtn = document.getElementById('add-line');
const productList = document.getElementById('product-list'); // Définie la liste des articles

let products = [];

// Charger les articles disponibles
fetch('/api/products/')
    .then(res => res.json())
    .then(data => {
        products = data;

        // Affiche la liste des produits
        data.forEach(product => {
            const li = document.createElement('li');
            li.textContent = `${product.name} ${product.description} ${product.quantity} en stock - ${product.price} €`;
            productList.appendChild(li);
        });

        // Ajouter la première ligne
        addRequestLine();
    });

// Ajouter une ligne de demande
addLineBtn.addEventListener('click', () => {
    addRequestLine();
});

function addRequestLine() {
    const line = document.createElement('div');
    line.classList.add('request-line');

    // Créer un label pour les titres si c'est la première ligne
    if (requestLinesContainer.children.length === 0) {
        const titles = document.createElement('div');
        titles.innerHTML = `<strong>Article</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>Quantité</strong>`;
        requestLinesContainer.appendChild(titles);
    }

    // Select produit
    const select = document.createElement('select');
    select.className = 'product-select';
    select.required = true;
    products.forEach(p => {
        const option = document.createElement('option');
        option.value = p.id;
        option.textContent = p.name;
        select.appendChild(option);
    });

    // Input quantité
    const input = document.createElement('input');
    input.type = 'number';
    input.min = 1;
    input.className = 'quantity-input';
    input.required = true;

    // Bouton de suppression
    const removeBtn = document.createElement('button');
    removeBtn.textContent = '❌';
    removeBtn.type = 'button';
    removeBtn.style.backgroundColor = '#f99';
    removeBtn.onclick = () => line.remove();

    // Ajouter au DOM
    line.appendChild(select);
    line.appendChild(input);
    line.appendChild(removeBtn);
    requestLinesContainer.appendChild(line);
}

// Soumettre le formulaire
form.addEventListener('submit', (e) => {
    e.preventDefault();
    message.textContent = '';

    const selects = form.querySelectorAll('.product-select');
    const quantities = form.querySelectorAll('.quantity-input');

    let requests = [];

    for (let i = 0; i < selects.length; i++) {
        const productId = selects[i].value;
        const quantity = quantities[i].value;

        if (productId && quantity > 0) {
            requests.push(fetch('/api/requests/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({
                    product: productId,
                    quantity_requested: quantity,
                })
            }));
        }
    }

    Promise.all(requests)
        .then(responses => {
            const allOk = responses.every(res => res.ok);
            if (allOk) {
                message.textContent = 'Toutes les demandes ont été envoyées avec succès.';
                requestLinesContainer.innerHTML = '';
                addRequestLine(); // Réinitialiser le formulaire
                fetchUserRequests();
            } else {
                message.textContent = 'Une ou plusieurs demandes ont échoué.';
            }
        });
});

// Affiche les demandes existantes
function fetchUserRequests() {
    fetch('/api/requests/')
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('requests-list');
            list.innerHTML = '';
            data.forEach(req => {
                const li = document.createElement('li');
                li.textContent = `${req.product.name} — Quantité: ${req.quantity_requested} — Statut: ${req.status_display || req.status}`;
                list.appendChild(li);
            });
        });
}

// Récupérer le CSRF token
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

fetchUserRequests();

Système de gestion d'inventaire :

Une application Django de gestion d'inventaire avec interface utilisateur en HTML, css et Javascript  permettant aux utilisateurs de consulter les produits et faire des demandes.

Stack technique :

Backend : Django, Django REST Framework
Frontend : HTML + JavaScript Vanilla
Base de données : SQLite (par défaut mais  modifiable)
Authentification : Auth Django (pour le login/logout)
API : RESTful via `ModelViewSet`
Environnement : Python 3.10+ avec `venv`

Structure du projet :

inventory_system/
-- inventory_system/ # Paramétrage global Django (settings, urls, etc.)
-- inventory/ # Application principale : modèles, vues, templates
---- models.py
---- views.py
---- serializers.py
---- templates/
---- static/
-- manage.py
-- requirements.txt
-- README.md

---

Instruction pour lancer le projet en local (via `venv`)

#1. Dupliquer le dépôt

```bash
git clone https://github.com/MartialMertzig/Deletec.git
cd inventory-system

## 2. Créer un environnement virtuel

python -m venv venv
source venv/bin/activate        # Pour macOS

venv\Scripts\activate           # Pour Windows

### 3. Installer les dépendances avec le pip

pip install -r requirements.txt

#### 4 Lancer le serveur SQLite (par défaut)

python manage.py migrate
python manage.py runserver

##### 5. Créer un utilisateur admin

python manage.py createsuperuser

#Ton projet est maintenant lancé. Accède à l'application à cette adresse :

http://127.0.0.1:8000/

#Accès et autentification

Interface de gestion : http://127.0.0.1:8000/admin/
Page de connexion : /login/
Page de déconnexion : /logout/
Interface de demande produit : /inventaire/
Accueil API : /api/

#Framework

Django>=4.0
djangorestframework

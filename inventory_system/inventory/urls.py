from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductViewSet, ProductRequestViewSet

# Génére les endpoints API REST pour mes vues en viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet) # API des produits
router.register(r'requests', ProductRequestViewSet, basename='requests') # API des demandes produits

urlpatterns = [
    path('', views.index, name='index'), # Page d'accueil
    path('api/', include(router.urls)), # API

    # Utilisation des vues Django par défaut pour le login et le logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Interface client protégée par Login_required
    path('inventaire/', views.product_list, name='liste_produit'),
]

# Mode DEBUG en développement local : Fichiers statiques depuis STATICFILES_DIRS
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
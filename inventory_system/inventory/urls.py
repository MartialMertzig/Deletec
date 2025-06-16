from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .import views
from .views import ProductViewSet, ProductRequestViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'requests', ProductRequestViewSet, basename='requests')

urlpatterns = [
    path('', views.index, name='index'), # Accueil
    path('api/', include(router.urls)), #API

    #Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Produits
    path('inventaire/', views.product_list, name='liste_produit'),
]
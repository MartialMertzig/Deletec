from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
from .views import ProductViewSet, ProductRequestViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'requests', ProductRequestViewSet, basename='requests')

urlpatterns = [
    path('', views.index, name='index'), # Accueil
    path('api/', include(router.urls)), #API
]
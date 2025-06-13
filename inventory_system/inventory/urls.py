from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import ProductViewSet, ProductRequestViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'requests', ProductRequestViewSet)

urlpartterns = [
    path('api/', include(router.urls)),
]
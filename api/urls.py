from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, BuyerViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'buyers', BuyerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
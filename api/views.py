from rest_framework import viewsets
from .models import Supplier, Buyer, Product, Order
from .serializers import SupplierSerializer, BuyerSerializer, ProductSerializer, OrderSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
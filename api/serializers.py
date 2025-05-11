from rest_framework import serializers
from .models import Supplier, Buyer, Product, Order

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
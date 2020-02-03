from rest_framework import serializers
from web.models import ProductDetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductDetails
        fields = ['productName', 'productDesc', 'productPrice']
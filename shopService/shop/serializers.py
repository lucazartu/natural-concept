from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', )
        read_only_fields = ('id', )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'slug', 'description', 'price', 'stock', 'available', )
        read_only_fields = ('id', )
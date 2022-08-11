from rest_framework import serializers
from .models import Category,Book,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        field='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        field='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        field='__all__'


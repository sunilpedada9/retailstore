from django.db.models import fields
from rest_framework import serializers
from store.models import Category

# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
    
    def create(self, validated_data):
       Category_data=Category(**validated_data)
       Category_data.save()
       return Category_data



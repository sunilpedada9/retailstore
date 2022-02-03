from django.db.models import fields
from rest_framework import serializers
from store.models import Item
from store.models import Category

# Create item serializer
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields="__all__"
    
    # def validate(self,data):
    #     in_category=Category.objects.get(id=data.get("category"))
    #     if not in_category:
    #         raise serializers.ValidationError("Please enter valid caategory!.")
    #     return data

    def create(self,validated_data):
        item_data=Item(**validated_data)
        item_data.save()
        return item_data

    def update(self,instance,validated_data):
        instance.category=validated_data.get("category",instance.category)
        instance.item_name=validated_data.get("item_name",instance.item_name)
        instance.price=validated_data.get("price",instance.price)
        instance.save()
        return instance
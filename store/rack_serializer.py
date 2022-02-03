from django.db.models.fields import Field
from rest_framework import serializers
from store.models import Rack,Product
from django.db.models import Q

# Create serializer for rack model
class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rack
        fields="__all__"

    def validate(self,data):
        try:
            item_valid=Product.objects.get(Q(id=data["product"].id),Q(category=data["category"].id),~Q(status_id=3))
        except Product.DoesNotExist:
            raise serializers.ValidationError("Please enter valid product and category!")
        return data
        
    def create(self,validated_data):
        print("ss",validated_data)
        rack_data=Rack(**validated_data)
        rack_data.save()
        return rack_data

    def update(self, instance, validated_data):
        instance.product=validated_data.get("product",instance.product)
        instance.category=validated_data.get("category",instance.category)
        instance.quantity=validated_data.get("quentity",instance.quantity)
        return instance
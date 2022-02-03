from django.db.models.fields import Field
from rest_framework import serializers
from store.models import Rack,Item
from django.db.models import Q

# Create serializer for rack model
class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rack
        fields="__all__"

    def validate(self,data):
        try:
            item_valid=Item.objects.get(Q(id=data["item"].id),Q(category=data["category"].id),~Q(status_id=3))
        except Item.DoesNotExist:
            raise serializers.ValidationError("Please enter valid item and category!")
        return data
        
    def create(self,validated_data):
        print("ss",validated_data)
        rack_data=Rack(**validated_data)
        rack_data.save()
        return rack_data

    def update(self, instance, validated_data):
        instance.item=validated_data.get("item",instance.item)
        instance.category=validated_data.get("category",instance.category)
        instance.quantity=validated_data.get("quentity",instance.quantity)
        return instance
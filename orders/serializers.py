from rest_framework import serializers
from .models import Orderuser, Productinorder

class ProductinorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productinorder
        fields = ('__all__')

class OrderuserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
    class Meta:
        model = Orderuser
        fields = ('__all__')
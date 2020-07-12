from rest_framework import serializers
from .models import Orderuser, Productinorder


class ProductinorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productinorder
        fields = ('__all__')

class OrderuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderuser
        fields = ('__all__')
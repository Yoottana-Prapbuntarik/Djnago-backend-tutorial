from rest_framework import permissions, viewsets
from .serializers import OrderuserSerializer, ProductinorderSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Orderuser, Productinorder

# created new order user


class CreateproductViewSet(viewsets.ModelViewSet):
    queryset = Orderuser.objects.all()
    permissions = [
        permissions.AllowAny

    ]
    serializer_class = OrderuserSerializer

# product in order
class ProductinorderViewSet(viewsets.ModelViewSet):
    queryset = Productinorder.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = ProductinorderSerializer

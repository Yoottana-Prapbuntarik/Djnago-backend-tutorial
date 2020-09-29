from rest_framework import permissions, viewsets
from .serializers import OrderuserSerializer, ProductinorderSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Orderuser, Productinorder
from knox.auth import TokenAuthentication
# created new order user


class CreateproductViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permissions = [
        permissions.AllowAny
    ]
    queryset = Orderuser.objects.all()
    serializer_class = OrderuserSerializer

# product in order


class ProductinorderViewSet(viewsets.ModelViewSet):
    queryset = Productinorder.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = ProductinorderSerializer

    # def get_serializer_context(self, context):
    #     context.update({
    #         'request': self.request,
    #     })
    #     return context

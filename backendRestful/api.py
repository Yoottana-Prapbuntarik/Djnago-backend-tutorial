from backendRestful.models import Allproduct
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import AllproductSerializer

# Viewset


class AllproductViewSet(viewsets.ModelViewSet):
    queryset = Allproduct.objects.filter(published=True)
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        req = self.request
        queryset = super().get_queryset()
        product_type = req.query_params.get('type')
        if product_type:
            return queryset.filter(product_name=product_type)
        else:
            return queryset
    serializer_class = AllproductSerializer

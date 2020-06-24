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
    serializer_class = AllproductSerializer
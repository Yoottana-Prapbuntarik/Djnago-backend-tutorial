from backendRestful.models import Allproduct, UserAuth
from rest_framework import viewsets, permissions
from .serializers import AllproductSerializer, UserSerializer 
# Viewset 
class AllproductViewSet(viewsets.ModelViewSet):
    queryset = Allproduct.objects.filter(published=True)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AllproductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserAuth.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
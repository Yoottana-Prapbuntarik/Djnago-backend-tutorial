from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework import status


# Register api 
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"data": "Created User Successful.", "token": AuthToken.objects.create(user)[1]}, status=status.HTTP_201_CREATED)


# Login api

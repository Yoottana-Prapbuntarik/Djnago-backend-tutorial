# import rest framework
# import modeal 
from rest_framework  import serializers
from .models import Allproduct, UserAuth
from django.contrib.auth.hashers import PBKDF2PasswordHasher

class AllproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allproduct
        fields = '__all__'        

class UserSerializer(serializers.ModelSerializer, PBKDF2PasswordHasher):
    class Meta:
        model = UserAuth
        fields = '__all__'
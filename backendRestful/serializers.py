# import rest framework
# import modeal 
from rest_framework  import serializers
from .models import Allproduct

class AllproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allproduct
        fields = '__all__'        

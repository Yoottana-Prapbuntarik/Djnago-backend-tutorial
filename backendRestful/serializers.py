# import rest framework
# import modeal 
from rest_framework  import serializers
from .models import Allproduct
from versatileimagefield.serializers import VersatileImageFieldSerializer

class AllproductSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = Allproduct
        fields = '__all__'        

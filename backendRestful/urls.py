from django.urls import path
from rest_framework import routers
from .api import AllproductViewSet

router = routers.DefaultRouter()

router.register('api/product',AllproductViewSet,'product')
urlpatterns = router.urls
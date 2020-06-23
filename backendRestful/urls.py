from django.urls import path
from rest_framework import routers
from .api import AllproductViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('api/product',AllproductViewSet,'product')
router.register('api/user',UserViewSet,'user')
urlpatterns = router.urls
from django.urls import path
from rest_framework import routers
from .api import CreateproductViewSet, ProductinorderViewSet

router = routers.DefaultRouter()

router.register('api/orders',CreateproductViewSet,'orders')
router.register('api/ordersproduct',ProductinorderViewSet,'product_in_orders')

urlpatterns = router.urls
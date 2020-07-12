from django.urls import path
from rest_framework import routers
from .api import AllproductViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register('api/product',AllproductViewSet,'product')
router.register('api/product',AllproductViewSet,{'type':'type'})

urlpatterns = router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
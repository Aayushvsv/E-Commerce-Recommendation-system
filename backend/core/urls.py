# core/urls.py

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserInteractionViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'interactions', UserInteractionViewSet)

urlpatterns = router.urls
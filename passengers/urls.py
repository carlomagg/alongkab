from rest_framework import routers
from .api import PassengersViewSet

router = routers.DefaultRouter()
router.register('api/passengers', PassengersViewSet, 'passengers')

urlpatterns = router.urls 
from rest_framework import routers
from .api import DriversViewSet

router = routers.DefaultRouter()
router.register('api/drivers', DriversViewSet, 'drivers')

urlpatterns = router.urls
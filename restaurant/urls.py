from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet

router = DefaultRouter()
router.register("menu", MenuItemViewSet, basename="menu")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = router.urls

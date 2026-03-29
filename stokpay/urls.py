from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contributions.views import MemberViewSet, ContributionViewSet, StokvelViewSet, PayoutViewSet

router = DefaultRouter()
router.register(r'stokvels', StokvelViewSet)
router.register(r'members', MemberViewSet)
router.register(r'contributions', ContributionViewSet)
router.register(r'payouts', PayoutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

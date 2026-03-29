from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from contributions.views import MemberViewSet, ContributionViewSet, StokvelViewSet, PayoutViewSet

router = DefaultRouter()
router.register(r'stokvels', StokvelViewSet)
router.register(r'members', MemberViewSet)
router.register(r'contributions', ContributionViewSet)
router.register(r'payouts', PayoutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

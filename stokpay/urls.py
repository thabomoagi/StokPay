from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contributions.views import MemberViewSet, ContributionViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'contributions', ContributionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

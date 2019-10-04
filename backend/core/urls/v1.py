from rest_framework import routers
from django.urls import include, path
from core.views import UrlViewSet

router = routers.DefaultRouter()
router.register(r'urls', UrlViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


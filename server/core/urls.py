from django.urls import path, include
from rest_framework import routers

from server.core.views import RiskTypeView


router = routers.SimpleRouter()
router.register(r'risk', RiskTypeView, basename='risk')

urlpatterns = [
    path('', include(router.urls)),
]

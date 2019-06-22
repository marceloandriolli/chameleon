from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from server.core.views import RiskTypeView, FieldView


router = routers.SimpleRouter()
router.register(r'risk', RiskTypeView, basename='risk')
router.register(r'field', FieldView, basename='field')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Risk Type API')),
]

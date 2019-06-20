from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from server.core.models import RiskTypeModel
from server.core.serializer import RiskSerializer

class RiskTypeView(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = RiskTypeModel.objects.all()
    lookup_field = 'id'
    serializer_class =  RiskSerializer


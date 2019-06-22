from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from server.core.models import RiskTypeModel, FieldModel
from server.core.serializer import RiskSerializer, FieldSerializer

class RiskTypeView(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = RiskTypeModel.objects.all()
    lookup_field = 'id'
    serializer_class =  RiskSerializer

class FieldView(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = FieldModel.objects.all()
    lookup_field = 'id'
    serializer_class =  FieldSerializer
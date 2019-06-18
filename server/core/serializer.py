from rest_framework import serializers

from server.core.models import RiskTypeModel, FieldModel


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldModel
        fields = ('name', 'type', 'property')


class RiskSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = RiskTypeModel
        fields = ('name', 'fields')

    def create(self, validated_data):
        fields = validated_data.pop('fields')
        risk_type = RiskTypeModel.objects.create(**validated_data)
        for field in fields:
            risk_type.fields.add(FieldModel.objects.create(**field))
        
        return risk_type

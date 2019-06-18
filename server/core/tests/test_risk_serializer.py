from collections import OrderedDict
import pytest


from server.core.models import RiskTypeModel, FieldModel
from server.core.serializer import RiskSerializer



@pytest.mark.django_db
def test_create_risk_serializer():
    data = {
        'name': 'Car',
        'fields': [
            {'name': 'first name', 'type':'txt'},
            {'name': 'last name', 'type':'txt'},
            {'name': 'age', 'type':'num', 'property': {'number_type': 'int'}},
            {'name': 'area code', 'type':'num', 'property': {'number_type': 'int'}}
        ]
    }
    serializer = RiskSerializer(data=data)
    serializer.is_valid()
    serializer.save()
    assert serializer.is_valid()
    assert RiskTypeModel.objects.exists()

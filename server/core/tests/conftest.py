import pytest
from rest_framework.test import APIClient

from server.core.models import RiskTypeModel, FieldModel


@pytest.mark.django_db
@pytest.fixture(scope='function')
def client():
    return APIClient()


@pytest.mark.django_db
@pytest.fixture(scope='function')
def field_type():
    return FieldModel.objects.create(name='fist name', type='txt', property={'max_length': 55})

@pytest.mark.django_db
@pytest.fixture(scope='function')
def risk(field_type):
    risk = RiskTypeModel.objects.create(name='Test Risk Type')
    risk.fields.add(field_type)
    return risk

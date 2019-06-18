import pytest

from server.core.models import RiskTypeModel, FieldModel


@pytest.mark.django_db
@pytest.fixture(scope='function')
def risk():
    return RiskTypeModel.objects.create(name='Test Risk Type')


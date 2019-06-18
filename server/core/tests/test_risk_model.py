import pytest

from server.core.models import RiskTypeModel, FieldModel


@pytest.mark.django_db
def test_risk_model_str(risk):
    assert str(risk) == 'Test Risk Type'

    
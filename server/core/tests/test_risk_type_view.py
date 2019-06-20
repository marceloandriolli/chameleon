import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_get_valid_risk_type_list(client, risk):
    response = client.get(reverse('risk-list'), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_valid_risk_type_detail(client, risk):
    response = client.get(reverse('risk-detail', kwargs={'id': risk.id}), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3
    assert response.data.get('id') == risk.id

@pytest.mark.django_db
def test_get_invalid_risk_type_detail(client):
    response = client.get(reverse('risk-detail', kwargs={'id': 333}), format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_valid_risk_type(client):
    data = {
        'name': 'Car',
        'fields': [
            {'name': 'first name', 'type':'txt'},
            {'name': 'last name', 'type':'txt'},
            {'name': 'age', 'type':'num', 'property': {'number_type': 'int'}},
            {'name': 'area code', 'type':'num', 'property': {'number_type': 'int'}}
        ]
    }
    response = client.post(reverse('risk-list'), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 3


@pytest.mark.django_db
def test_create_invalid_risk_type(client):
    data = {
        'fields': [
            {'name': 'first name', 'type':'txt'},
        ]
    }
    response = client.post(reverse('risk-list'), data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_update_valid_risk_type(client, risk):
        data = {'name': 'vehicle'}
        response = client.put(reverse('risk-detail', kwargs={'id': risk.id}), data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

@pytest.mark.django_db
def test_update_invalid_risk_type(client, risk):
        data = {
            'fields': [
                {'name': 'first name', 'type':'txt'},
            ]
        }
        response = client.put(reverse('risk-detail', kwargs={'id': risk.id}), data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

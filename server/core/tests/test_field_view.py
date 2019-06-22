import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_get_valid_field_type_list(client, field_type):
    response = client.get(reverse('field-list'), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_valid_field_type_detail(client, field_type):
    response = client.get(reverse('field-detail', kwargs={'id': field_type.id}), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 4
    assert response.data.get('id') == field_type.id

@pytest.mark.django_db
def test_get_invalid_field_type_detail(client):
    response = client.get(reverse('field-detail', kwargs={'id': 333}), format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_create_valid_field_type(client):
    data = {'name': 'age', 'type':'num', 'property': {'number_type': 'int'}}
    response = client.post(reverse('field-list'), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 4

@pytest.mark.django_db
def test_create_invalid_field_type(client):
    data = {'name': 'age', 'property': {'number_type': 'int'}}
    response = client.post(reverse('field-list'), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 4

@pytest.mark.django_db
def test_update_valid_field_type(client, field_type):
    data = {'name': 'last name',}
    response = client.put(reverse('field-detail', kwargs={'id': field_type.id}), data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 4

@pytest.mark.django_db
def test_update_invalid_field_type(client, field_type):
    data = {'address': 'Balls Street',}
    response = client.put(reverse('field-detail', kwargs={'id': field_type.id}), data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


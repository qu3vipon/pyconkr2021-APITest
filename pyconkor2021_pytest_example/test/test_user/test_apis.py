import pytest
from django.apps import apps
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APIClient
from schema import Schema, And, Or

User = get_user_model()
UserProfile = apps.get_model('user', 'UserProfile')


# Original

@pytest.mark.django_db
class TestUser:
    user_credentials = {
        'username': 'qu3vipon',
        'password': 'pyconkor2021',
    }

    invalid_user_credentials = {
        'username': 'something',
        'password': 'wrong',
    }

    def test_user_login(self):
        client = APIClient()
        url = resolve_url('auth_login')
        response = client.post(url, self.user_credentials)

        assert response.status_code == status.HTTP_200_OK
        assert 'access_token' in response.data
        assert 'refresh_token' in response.data

        assert 'user' in response.data
        assert response.data['user']['username'] == 'qu3vipon'
        assert response.data['user']['email'] == 'qu3vipon@gmail.com'
        assert response.data['user']['is_staff'] is True

    def test_user_profile(self, force_login, user_one):
        client = force_login(user_one)
        url = resolve_url('user_self_profile')
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['user']['username'] == 'qu3vipon'
        assert response.data['user']['email'] == 'qu3vipon@gmail.com'
        assert response.data['user']['is_staff'] is True
        assert response.data['profile']['gender'] == 'M'
        assert response.data['profile']['gender'] in UserProfile.Gender
        assert response.data['profile']['date_of_birth'] == '1992-07-13'
        assert response.data['profile']['date_of_birth'] < str(UserProfile.MIN_DATE_OF_BIRTH)


# With Schema

@pytest.mark.django_db
class TestUserWithSchema:
    user_credentials = {
        'username': 'qu3vipon',
        'password': 'pyconkor2021',
    }

    invalid_user_credentails = {
        'username': 'something',
        'password': 'wrong',
    }

    def test_user_login(self):
        client = APIClient()
        url = resolve_url('auth_login')
        response = client.post(url, self.user_credentials)

        schema = Schema({
            'access_token': And(str, len),
            'refresh_token': And(str, len),
            'user': {
                'username': 'qu3vipon',
                'email': 'qu3vipon@gmail.com',
                'is_staff': True,
            }
        })

        assert response.status_code == status.HTTP_200_OK
        assert schema.is_valid(response.json())

    @pytest.mark.parametrize(
        'username, email, password',
        [
            ('qu3vipon', 'qu3vipon@gmail.com', 'pyconkor2021'),
            ('pyconkor2021', 'pyconkor2021@gmail.com', 'pyconkor2021'),
        ]
    )
    def test_user_login_parameterized(self, username, email, password):
        client = APIClient()
        url = resolve_url('auth_login')

        user_credentials = {
            'username': username,
            'password': password,
        }
        response = client.post(url, user_credentials)

        schema = Schema({
            'access_token': And(str, len),
            'refresh_token': And(str, len),
            'user': {
                'username': username,
                'email': email,
                'is_staff': bool,
            }
        })

        assert response.status_code == status.HTTP_200_OK
        assert schema.is_valid(response.json())

    @pytest.mark.parametrize(
        'user, username, email, is_staff, gender',
        [
            (pytest.lazy_fixture('user_one'), 'qu3vipon', 'qu3vipon@gmail.com', True, 'M'),
            (pytest.lazy_fixture('user_two'), 'pyconkor2021', 'pyconkor2021@gmail.com', False, 'F'),
        ]
    )
    def test_user_profile(self, force_login, user, username, email, is_staff, gender):
        client = force_login(user)
        url = resolve_url('user_self_profile')
        response = client.get(url)

        user_base_schema = Schema({
            'username': username,
            'email': email,
            'is_staff': is_staff,
        })

        user_profile_schema = Schema({
            'user': user_base_schema,
            'profile': {
                'gender':
                    And(
                        gender,
                        lambda g: g in UserProfile.Gender,
                    ),
                'date_of_birth':
                    Or(
                        And(
                            str,
                            lambda d: d < str(UserProfile.MIN_DATE_OF_BIRTH)
                        ),
                        None,
                    ),
            }
        })

        assert response.status_code == status.HTTP_200_OK
        assert user_profile_schema.is_valid(response.json())

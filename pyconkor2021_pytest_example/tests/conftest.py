import os

import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from rest_framework.test import APIClient
from user.models import UserProfile

from pyconkor2021_pytest_example.settings import BASE_DIR

User = get_user_model()


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        dir_path = os.path.join(BASE_DIR, f"tests/fixtures")
        files = os.listdir(dir_path)
        for file in files:
            call_command("loaddata", f"tests/fixtures/{file}")


@pytest.fixture(scope="session")
def force_login():
    def _force_login(user):
        client = APIClient()
        client.force_login(user)
        return client

    return _force_login


@pytest.fixture
def user_one():
    return User.objects.get(pk=1)


@pytest.fixture(autouse=True)
def user_two():
    user = User.objects.create(username="pyconkor2021", email="pyconkor2021@gmail.com")
    user.set_password("pyconkor2021")
    user.save()
    UserProfile.objects.create(user=user, gender="F")
    yield user

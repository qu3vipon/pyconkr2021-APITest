# shop list -> list type
# minimum price test
import pytest
from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APIClient
from schema import Schema


@pytest.mark.django_db
class TestProductWithSchema:
    def test_product_list(self):
        client = APIClient()
        url = resolve_url("shop_product_list")
        response = client.get(url)

        product_schema = {
            "name": str,
            "price": int,
            "discount_rate": float,
        }

        product_list_schema = Schema([product_schema])

        assert response.status_code == status.HTTP_200_OK
        assert product_list_schema.is_valid(response.json())

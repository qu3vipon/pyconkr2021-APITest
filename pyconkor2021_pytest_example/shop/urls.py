from django.urls import path

from .views import ProductListView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="shop_product_list"),
]

from django.urls import path

from .views import UserSelfProfileView

urlpatterns = [
    path("self/", UserSelfProfileView.as_view(), name="user_self_profile"),
]

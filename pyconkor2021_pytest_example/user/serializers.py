from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.models import UserProfile

User = get_user_model()


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "is_staff",
        ]


class UserSelfProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "gender",
            "date_of_birth",
        ]

    def to_representation(self, instance):
        user_base = UserBaseSerializer(instance.user).data
        profile = super().to_representation(instance)

        representation = {
            "user": user_base,
            "profile": profile,
        }
        return representation

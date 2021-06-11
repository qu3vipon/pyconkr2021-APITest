from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework.generics import get_object_or_404

from .models import UserProfile
from .serializers import UserSelfProfileSerializer

User = get_user_model()


class UserSelfProfileView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSelfProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

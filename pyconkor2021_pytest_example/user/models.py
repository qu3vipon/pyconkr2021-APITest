from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    MIN_DATE_OF_BIRTH = timezone.localdate()

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        NON_BINARY = 'N', 'Non-binary'
        TRANSGENDER = 'T', 'Transgender'
        INTERSEX = 'I', 'Intersex'
        __empty__ = '(Unknown)'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.__empty__)
    date_of_birth = models.DateField(blank=True, null=True, default=None)

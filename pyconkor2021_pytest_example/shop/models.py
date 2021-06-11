from django.db import models


class Product(models.Model):
    MINIMUM_PRICE = 500

    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField(default=0)
    discount_rate = models.FloatField(default=0)

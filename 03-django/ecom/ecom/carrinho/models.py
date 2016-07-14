from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    photo = models.ImageField(blank=True, upload_to='media')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Product({!r}, active={!r})'.format(self.name, self.active)


class Purchase(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)

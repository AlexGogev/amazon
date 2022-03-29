
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    price = models.IntegerField()
    favorite = models.ManyToManyField(User, default=None, blank=True, related_name="favorite")

    def __str__(self):
        return self.title
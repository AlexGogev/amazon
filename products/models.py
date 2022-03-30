
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=50)
    short_details = models.TextField()
    full_detail = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.URLField(max_length=2048, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    favorite = models.ManyToManyField(User, default=None, blank=True, related_name="favorite")

    def __str__(self):
        return self.title
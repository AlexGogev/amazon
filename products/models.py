
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=800)
    short_details = models.TextField()
    full_detail = models.TextField(blank=True, null=True)
    inside_box = models.TextField(default=None, blank=True)
    price = models.CharField(max_length=10)
    image = models.URLField(max_length=2048, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    favorite = models.ManyToManyField(User, default=None, blank=True, related_name="favorite")
    review_rating = models.CharField(max_length=20, default=None, blank=True)
    buy_link = models.URLField(max_length=2048, blank=True, null=True)
    Choices = (
        ("Technology", "Technology"),
        ("Books", "Books"),
        ("Clothing", "Clothing"),
        ("Home", "Home"),
        ("Games", "Games"),
        ("Health", "Health"),
        ("Skin", "Skin"),
        ("Health", "Health"),
        ("Makeup", "Makeup"),
        ("Lotions", "Lotions"),
        ("Shampoo", "Shampoo"),
        ("Food", "Food"),
    )

    category = models.CharField(max_length=100, choices=Choices, default="Select category")
    def __str__(self):
        return self.title

    # set redirect add this is to allow reverse when creating and updating
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-date_created"]
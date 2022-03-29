from django import forms
from. models import Product
from django.contrib.auth.models import User


class AddToFav(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title"]

from django.urls import path

from .views import *

urlpatterns = [
    path("", Listing.as_view(), name="index"),
    path("detail/<int:pk>", Detail.as_view(), name="detail"),
    path("add-to-fav/", add_to_fav, name="add-to-fav")
    ]
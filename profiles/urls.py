from django.urls import path

from .views import *

urlpatterns = [
    path("likes/", My_Likes.as_view(), name="profiles"),
   # path("add-to-fav/<int:pk>", Add_To_Fav.as_view(), name="add-to-fav")
    ]
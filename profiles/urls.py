from django.urls import path

from .views import *

urlpatterns = [
    path("likes/", My_Likes.as_view(), name="profiles"),
    path('add-to-fav/<int:id>/', add_to_fav, name="add-to-fav"), #id , capture the post id

    ]
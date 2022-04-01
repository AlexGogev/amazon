from django.urls import path

from .views import *

urlpatterns = [
    path("likes/", My_Likes, name="profiles"), #.as_view()
    path('add-to-fav/<int:id>/', add_to_fav, name="add-to-fav"), #id , capture the post id
    path('del-fav/<int:id>/', del_fav, name="del-fav")
    ]
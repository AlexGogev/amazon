from django.urls import path

from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("detail/<int:pk>", Detail.as_view(), name="detail"),
    ]
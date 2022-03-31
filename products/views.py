from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Product

from django.db.models import Q

class HomePageView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = "product"
    def get_queryset(self): # new
        return Product.objects.all()


class SearchResultsView(ListView): #https://learndjango.com/tutorials/django-search-tutorial
    model = Product
    template_name = 'products/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(title__icontains=query) | Q(short_details__icontains=query) | Q(full_detail__icontains=query)
        )
        return object_list

class Detail(DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = "product"





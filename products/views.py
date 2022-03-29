from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import AddToFav

class Listing(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "product"


class Detail(DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = "product"


@login_required
def add_to_fav(request):
    if request.method == "POST":
        form = AddToFav(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "products/detail.html", context)
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin  # requires login for class based views it is 1st inheritance
from django.contrib.auth.mixins import UserPassesTestMixin  # other people cant edit the post
from products.models import Product


class My_Likes(LoginRequiredMixin, ListView):
    model = Product
    template_name = "profiles/my-likes.html"
    context_object_name = "product"


    def get_queryset(self):
        return Product.objects.filter(favorite=self.request.user)


@login_required
def add_to_fav(request, id):
    post = get_object_or_404(Product, id=id)  # return item from Product and match id
    if post.favorite.filter(id=request.user.id): #check to see if already added
        post.favorite.remove(request.user)
    else:
        post.favorite.add(request.user)
    return redirect("detail", pk=post.id)
    #return HttpResponseRedirect(request.META["HTTP_REFERER"])







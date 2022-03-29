from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from. forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")  # getting the data
            print(str(username))  # getting the data
            messages.success(request, f" Your account has been created! You can log in as {username}!")
            # update now base.html template
            # { % if messages %}
            # { % for message in messages %}
            #  <div class ="alert alert-{{message.tags}}">
            # {{message}}
            # </div>
            # { % endfor %}
            # { % endif %}
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


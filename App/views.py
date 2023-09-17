from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import UserForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView,FormView

from .models import User
# Create your views here.
class HomeView(FormView):
    form_class = UserForm
    template_name = "App/home.html"
    success_url = "users"
    def form_valid(self, form):
        instance = form.save()
        return super().form_valid(form)
    # def get(self, request):
    #     form = UserForm()
    #     return render(request, "App/home.html", {'form':form})
    # def post(self, request):
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, "App/thank_you.html")

    #     else:
    #         return render(request, "App/home.html", {'form':form})


class UsersView(ListView):
    template_name = "App/users.html"
    model = User
    context_object_name = "users"
   
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     users = User.objects.all()
    #     context["users"] = users
    #     return context

class SingleUser(DetailView):
    template_name="App/singleuser.html"
    model = User
    context_object_name = "single_user"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_id = kwargs["id"]
    #     single_user = User.objects.get(pk=user_id)
    #     print(single_user.email)
    #     context["single_user"] = single_user
    #     return context
    

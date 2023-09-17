from django.urls import path

from .import views
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('users',views.UsersView.as_view(), name="users"),
    path('user/<int:pk>',views.SingleUser.as_view(), name="user"),

] 
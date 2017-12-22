from django.urls import path
from django.contrib.auth.views import login, logout

from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', login, {"template_name":"accounts/login.html"},  name='login'),
    path('logout/', logout, {"next_page":"core:home"},  name='logout'),
    path("register/", views.register, name="register")
]

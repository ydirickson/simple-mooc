from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path('', views.courses, name='index'),
    path("<slug:slug>", views.detail, name="detail"),
    path("<slug:slug>/inscricao", views.enrollment, name="enrollment")

]

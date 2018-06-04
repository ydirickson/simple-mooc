from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path('', views.courses, name='index'),
    path("<slug:slug>", views.detail, name="detail"),
    path("<slug:slug>/inscricao", views.enrollment, name="enrollment"),
    path("<slug:slug>/cancelar-inscricao", views.undo_enrollment, name="undo-enrollment"),
    path("<slug:slug>/anuncios/", views.announcements, name="announcements"),
    path("<slug:slug>/anuncio/<int:id>", views.show_announcement, name="show-announcement")

]

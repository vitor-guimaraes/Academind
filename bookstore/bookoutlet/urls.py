from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail, name="book-detail")
]

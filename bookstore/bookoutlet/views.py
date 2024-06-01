from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg

from . models import Book


def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "bookoutlet/index.html", {
        "books": books,
        "total_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except: raise Http404()
    book = get_object_or_404(Book, slug=slug)

    return render(request, "bookoutlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })
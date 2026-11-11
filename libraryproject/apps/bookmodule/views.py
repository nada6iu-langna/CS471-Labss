from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def links(request):
    return render(request, 'bookmodule/links.html')
# Lab 5 - Task 2
def formatting(request):
    return render(request, 'bookmodule/formatting.html')
# Lab 5 - Task 3
def listing(request):
    return render(request, 'bookmodule/listing.html')
# Lab 5 - Task 4
def tables(request):
    return render(request, 'bookmodule/tables.html')
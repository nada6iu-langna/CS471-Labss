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
# Lab 6 - Search Form
def search(request):

    if request.method == "POST":
        string = (request.POST.get('keyword') or '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Filter books
        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')
# Lab 6 - Task 2
def __getBooksList():
    book1 = {
        'id': 12344321,
        'title': 'Continuous Delivery',
        'author': 'J.Humble and D. Farley'
    }

    book2 = {
        'id': 56788765,
        'title': 'Reversing: Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }

    book3 = {
        'id': 43211234,
        'title': 'The Hundred-Page Machine Learning Book',
        'author': 'Andriy Burkov'
    }

    return [book1, book2, book3]
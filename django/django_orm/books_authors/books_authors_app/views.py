from django.shortcuts import render, redirect
from .models import Book, Author
# Create your views here.

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    
    return render(request, "index.html", context)

def author(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def add_book(request):
    book=Book()
    book.title = request.POST.get('title')
    book.desc = request.POST.get('description')
    book.save()
    return redirect('/')

def add_author(request):
    author=Author()
    author.first_name = request.POST.get('first_name')
    author.last_name = request.POST.get('last_name')
    author.notes = request.POST.get('notes')
    author.save()
    return redirect('/authors')

def book_page(request, num):
    context = {
        "book": Book.objects.get(id=num),
        "authors": Author.objects.filter(books=num),
        "all_authors": Author.objects.all()
    }
    return render(request,"book_page.html", context)

def author_page(request, num):
    context = {
        "author": Author.objects.get(id=num),
        "books":  Book.objects.filter(author=num),
        "all_books": Book.objects.all()
    }

    return render(request,"author_page.html", context)

def add_author_to_book(request,num):
    this_book = Book.objects.get(id=num)
    author = request.POST.get("authordropdown")
    this_book.author.add(author)
    return redirect('/')

def add_book_to_author(request,num):
    this_author = Author.objects.get(id=num)
    book = request.POST.get("bookdropdown")
    this_author.books.add(book)
    return redirect('/authors')





from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, Redaction, Friend
from django.shortcuts import redirect


def books_list(request):
    return HttpResponse('/index/ - для просмотра библиотеки; /redactions/ - для просмотра издательств; /friends/ - для просмотра друзей; /admin/ - для входа в админ. панель')

def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def redactions(request):
    template = loader.get_template('redactions.html')
    redactions = Redaction.objects.all()
    books = Book.objects.all()
    redactions_data = {
        "redactions": redactions,
        "books": books,
    }
    return HttpResponse(template.render(redactions_data, request))

def friends(request):
    template = loader.get_template('friends.html')
    friends = Friend.objects.all()
    books = Book.objects.all()
    friends_data = {
        "friends": friends,
        "books": books,
    }
    return HttpResponse(template.render(friends_data, request))
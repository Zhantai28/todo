from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, BookStore


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})


def second(request):
    return HttpResponse('test 2 page')


def bookStore(request):
    book_list = BookStore.objects.all()
    return render(request, 'books.html', {"book_list": book_list})


def add_todo(request):
    form = request.POST
    todo = ToDo(text=form['todo_text'])
    todo.save()

    return redirect(test)


def book_add(request):
    return render(request, 'books-add.html')


def add_book(request):
    form = request.POST
    bookstor = BookStore(title=form['book-title'], subtitle=form['book-subtitle'],
                         description=form['book-description'], price=form['book-price'],
                         genre=form['book-genre'], author=form['book-author'], year=form['book-year'])
    bookstor.save()

    return redirect(bookStore)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()

    return redirect(test)

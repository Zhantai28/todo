from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, BookStore


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'todo.html', {"todo_list": todo_list})


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


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    if todo.is_favorite:
        todo.is_favorite = False
    else:
        todo.is_favorite = True
    todo.save()
    return redirect(test)


def delete_book(request, id):
    book = BookStore.objects.get(id=id)
    book.delete()

    return redirect(bookStore)


def favorite_book(request, id):
    book = BookStore.objects.get(id=id)
    if book.is_favorite:
        book.is_favorite = False
    else:
        book.is_favorite = True
    book.save()
    return redirect(bookStore)


def book_info(request, id):
    book = BookStore.objects.get(id=id)
    return render(request, 'book-detail.html', {'book': book})


def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

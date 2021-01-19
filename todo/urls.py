"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('todo/', test, name='test'),
    path('book-store/', bookStore, name='bookstore'),
    path('add-todo/', add_todo, name='add-todo'),
    path('book-add/', book_add, name='book-add'),
    path('add-book', add_book, name='book-add-on-the-site'),
    path('delete-todo/<id>/', delete_todo, name='delete-todo'),
    path('mark-todo/<id>/', mark_todo, name='mark-todo'),
    path('delete-book/<id>/', delete_book, name='delete-book'),
    path('favorite-book/<id>/', favorite_book, name='favorite-book'),
    path('book-info/<id>/', book_info, name='info-book'),
    path('close-todo/<id>/', close_todo, name='close-todo')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100, verbose_name='Задача')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    is_closed = models.BooleanField(default=False, verbose_name='Выполнена')
    is_favorite = models.BooleanField(default=False, verbose_name='Избранная')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

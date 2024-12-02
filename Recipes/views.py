from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Recipe


def recipes_view(request):
    # Исправленный SQL-запрос с указанием первичного ключа (id)
    recipes = Recipe.objects.raw('SELECT * FROM recipes')

    # Отправляем результат в шаблон
    return render(request, 'index.html', {'recipes': recipes})


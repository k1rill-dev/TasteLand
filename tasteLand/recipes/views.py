from django.shortcuts import render, get_object_or_404
from .models import Recipes, Category
import random

#TODO: переделать карусель и дописать главную страницу(DONE)

#TODO: дописать страницы О сайте, Контакты, Рецепт. Добавить фотки на главную страницу(DONE)

#TODO: доделать страницу с рецептом(DONE)

#TODO: переписать модели бд(DONE)

def home_page(request):
    fir, sec, thrd = Recipes.objects.order_by('?')[:3]
    recipes = Recipes.objects.all()[:6]
    cats = Category.objects.all()[:6]
    context = {
        'title': 'Главная страница',
        'rec': recipes,
        'fir_rec_carousel': fir,
        'sec_rec_carousel': sec,
        'thrd_rec_carousel': thrd,
        'cats': cats,
    }
    return render(request, 'recipes/index.html', context)

def view_categories(request, cat_id):
    recipes = Recipes.objects.filter(pk=cat_id)
    cat = Category.objects.get(pk=cat_id)
    context = {
        'rec': recipes,
        'cat': cat,
        'title': 'Категория'
    }
    return render(request, 'recipes/category.html', context)

def recipe(request, rec_id):
    recipe = get_object_or_404(Recipes, pk=rec_id)
    return render(request, 'recipes/recipes.html', {'title': 'Рецепты', 'rec': recipe})

def contacts(request):
    return render(request, 'recipes/contacts.html', {'title': 'Контакты'})

def about(request):
    return render(request, 'recipes/about.html', {'title': 'О сайте'})




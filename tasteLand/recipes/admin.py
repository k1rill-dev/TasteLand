from django.contrib import admin

from .models import Recipes, Category

admin.site.register(Recipes)
admin.site.register(Category)

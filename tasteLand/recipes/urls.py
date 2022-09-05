from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('recipes/<int:rec_id>', recipe, name='recipe'),
    path('category/<int:cat_id>/', view_categories, name='category'),

]
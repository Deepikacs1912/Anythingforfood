from django.contrib import admin

from .models import Ingredient, Recipe

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
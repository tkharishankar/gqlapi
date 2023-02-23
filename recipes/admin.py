from django.contrib import admin

from recipes.models import Recipe, Ingredient, Step

# Register your models here.
recipeModels = [Recipe, Ingredient, Step]
admin.site.register(recipeModels)

from django.db import models


# Create your models here.
class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    original_url = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Ingredient(models.Model):
    ingredients_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Step(models.Model):
    steps_id = models.AutoField(primary_key=True)
    timer = models.CharField(max_length=100)
    step = models.CharField(max_length=100)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

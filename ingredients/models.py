from django.db import models


# Create your models here.
class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

# Generated by Django 4.1.5 on 2023-02-23 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('original_url', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('steps_id', models.AutoField(primary_key=True, serialize=False)),
                ('timer', models.CharField(max_length=100)),
                ('step', models.CharField(max_length=100)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('ingredients_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-12-02 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CookingSteps',
            new_name='CookingStep',
        ),
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.RenameModel(
            old_name='Recipes',
            new_name='Recipe',
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]

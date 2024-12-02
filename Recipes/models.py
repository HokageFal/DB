from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'ingredients'

    def __str__(self):
        return self.name or "Unnamed Ingredient"


class Recipe(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    cuisine = models.CharField(max_length=50, blank=True, null=True)
    difficulty_level = models.CharField(max_length=20, blank=True, null=True)
    prep_time = models.IntegerField(blank=True, null=True)
    cook_time = models.IntegerField(blank=True, null=True)
    serving_size = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    class Meta:
        db_table = 'recipes'

    def __str__(self):
        return self.title or "Untitled Recipe"


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return f"Review for {self.recipe} - {self.rating} Stars"


class Users(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username or "Anonymous User"

class CookingStep(models.Model):
    recipe = models.ForeignKey(Recipe, models.CASCADE, blank=True, null=True)
    step_number = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'cooking_steps'

    def __str__(self):
        return f"Step {self.step_number} for Recipe {self.recipe}"
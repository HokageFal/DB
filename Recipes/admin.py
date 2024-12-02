from django.contrib import admin
from .models import Ingredient, Recipe, Review, Users, CookingStep

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Отображаем имя и категорию ингредиента
    search_fields = ('name',)  # Возможность поиска по имени ингредиента

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'cuisine', 'difficulty_level', 'prep_time', 'cook_time', 'serving_size', 'image')  # Отображаем изображение
    search_fields = ('title',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'rating', 'comment')  # Отображаем рецепт, рейтинг и комментарий
    search_fields = ('recipe__title',)  # Поиск по названию рецепта

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'registration_date')  # Отображаем имя пользователя, email и дату регистрации
    search_fields = ('username',)  # Поиск по имени пользователя

class CookingStepAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'step_number', 'description')  # Отображаем рецепт, номер шага и описание
    search_fields = ('recipe__title',)  # Поиск по названию рецепта

# Регистрация моделей в админке
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(CookingStep, CookingStepAdmin)

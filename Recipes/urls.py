from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.recipes_view, name='index'),
]

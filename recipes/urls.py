from django.urls import path
from .import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('receitas/categoria/<int:category_id>/', views.category, name='category'),
    path('receitas/<int:id>/', views.recipe, name='recipe'),
]
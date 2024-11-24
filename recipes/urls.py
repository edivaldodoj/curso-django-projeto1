from django.urls import path
from .import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('receitas/<int:id>/', views.recipe, name='recipe'),
]